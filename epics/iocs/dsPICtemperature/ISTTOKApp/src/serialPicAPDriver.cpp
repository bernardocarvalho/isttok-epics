/*************************************************************************
 *
 * Project       : ISTTOK slow Control
 *
 * Description   : serialPicAPDriverApp.cpp
 *              based on testAsynPortDriver.cpp
 *
 * Author        : Bernardo Carvalho (IPFN-IST)
 *
 * Edited        : Gonçalo Quintal   (IPFN-IST)
 *
 * Copyright (c) : (IPFN-IST)
 * Created 25-Feb-2013
 * Last Edit 22-Mar-2014
 *
 * SVN keywords
 * $Date: 2014-08-17 18:30:17 +0100 (Sun, 17 Aug 2014) $
 * $Revision: 6572 $
 * $URL: http://metis.ipfn.ist.utl.pt:8888/svn/cdaq/ISTTOK/Software/EPICS/ISTTOKcontrol/branches/quintal/ISTTOKApp/src/serialPicAPDriver.cpp $
 *
 *
 ************************************************************************/
#include <epicsStdlib.h>
#include <string.h>

//#include <errno.h>
//#include <math.h>

//#include <epicsTypes.h>
//#include <epicsTime.h>
//#include <epicsThread.h>
//#include <epicsString.h>
#include <epicsTimer.h>
//#include <epicsMutex.h>
//#include <epicsEvent.h>
#include <iocsh.h>

// #include "serialPicAPDriver.h"
#include "serialPicAPDriver.h"
#include <epicsExport.h>
#include <asynOctetSyncIO.h>

#define BUFLEN 512
#define WRITE_TIMEOUT 2.0
//#define EOS_STR "\r\n"
#define EOS_STR "\n"
#define NPAR 50    // max parameters in read message
#define PARMAX  20 // max no of chars per parameter

static const char *driverName="serialPicAPDriver";
void blockReadTask(void *drvPvt);

/** Constructor for the serialPicAPDriver class.
 * Calls constructor for the asynPortDriver base class.
 * \param[in] portName The name of the asyn port driver to be created.
 * \param[in] maxChars The maximum  number of .... */
serialPicAPDriver::serialPicAPDriver(const char *portName, const char *serialPortName, int maxChars)
  : asynPortDriver(portName,
		   1, /* maxAddr */
		   (int)NUM_PIC_PARAMS,
		   //		   asynInt32Mask | asynFloat64Mask | asynFloat64ArrayMask | asynEnumMask | asynDrvUserMask, /* Interface mask */
		   //asynInt32Mask | asynFloat64Mask | asynFloat64ArrayMask | asynEnumMask,  /* Interrupt mask */
		   asynInt32Mask | asynFloat64Mask | asynDrvUserMask, /* Interface mask */
		   asynInt32Mask | asynFloat64Mask ,  /* Interrupt mask */
		   ASYN_CANBLOCK, /* asynFlags.  This driver does block and it is not multi-device, ASYN_MULTIDEVICE=0  */
		   1, /* Autoconnect */
		   0, /* Default priority */
		   0) /* Default stack size*/
{
  asynStatus status;
  //int i;
  const char *functionName = "serialPicAPDriver";

  /* Connect to the port */
  status = pasynOctetSyncIO->connect(serialPortName, 0, &this->pasynUserSPort, NULL);
  if (status) {
    printf("%s:%s: pasynOctetSyncIO->connect failure, port:%s status=%d\n", driverName, functionName, serialPortName, status);
    return;
  }
  else
    printf("%s:%s: pasynOctetSyncIO->connect OK, status=%d\n", driverName, functionName, status);

  status = pasynOctetSyncIO->setInputEos(this->pasynUserSPort, EOS_STR, strlen(EOS_STR));
  if (status) {
    printf("%s:%s: pasynOctetSyncIO->setInputEos failure,  status=%d\n", driverName, functionName, status);
    return;
  }
  status = pasynOctetSyncIO->setOutputEos(this->pasynUserSPort, EOS_STR,  strlen(EOS_STR));
  if (status) {
    printf("%s:%s: pasynOctetSyncIO->setOutputEos failure,  status=%d\n", driverName, functionName, status);
    return;
  }


  eventId_ = epicsEventCreate(epicsEventEmpty);
  createParam(P_UpTimeString,             asynParamInt32,         &P_UpTime);
  //Creation of 4 variables for valve control 
  createParam(P_ValveChange1String,       asynParamInt32,         &P_ValveChange1);
  createParam(P_ValveState1String,        asynParamInt32,         &P_ValveState1);
  createParam(P_ValveChange2String,       asynParamInt32,         &P_ValveChange2);
  createParam(P_ValveState2String,        asynParamInt32,         &P_ValveState2);
  createParam(P_ValveChange3String,       asynParamInt32,         &P_ValveChange3);
  createParam(P_ValveState3String,        asynParamInt32,         &P_ValveState3);
  createParam(P_ValveChange4String,       asynParamInt32,         &P_ValveChange4);
  createParam(P_ValveState4String,        asynParamInt32,         &P_ValveState4);
  //Creation of 8 variables for temperature
  createParam(P_Temperature0String,       asynParamFloat64,       &P_Temperature0);
  createParam(P_Temperature1String,       asynParamFloat64,       &P_Temperature1);
  createParam(P_Temperature2String,       asynParamFloat64,       &P_Temperature2);
  createParam(P_Temperature3String,       asynParamFloat64,       &P_Temperature3);
  createParam(P_Temperature4String,       asynParamFloat64,       &P_Temperature4);
  createParam(P_Temperature5String,       asynParamFloat64,       &P_Temperature5);
  createParam(P_Temperature6String,       asynParamFloat64,       &P_Temperature6);
  createParam(P_Temperature7String,       asynParamFloat64,       &P_Temperature7);
  //Creation of 4 variables for pressure
  createParam(P_Pressure1String,          asynParamFloat64,       &P_Pressure1);
  createParam(P_Pressure2String,          asynParamFloat64,       &P_Pressure2);
  createParam(P_Pressure3String,          asynParamFloat64,       &P_Pressure3);
  createParam(P_Pressure4String,          asynParamFloat64,       &P_Pressure4);
  //Creation of 1 variable for periode
  createParam(P_Period0String,            asynParamFloat64,       &P_Period0);

  //createParam(P_TimePerDivString,         asynParamFloat64,       &P_TimePerDiv);

  /* Set the initial values of some parameters */
  //  setIntegerParam(P_MaxPoints,         maxPoints);
  //setIntegerParam(P_Run,               0);
  
  //This seet forces d value of P_Valve* to 1, sending one message to dsPIC to open the valve
  //This happens always in the startup of ioc program 
  //setIntegerParam(P_Valve1,  1);
  //setIntegerParam(P_Valve2,  1);
  //setIntegerParam(P_Valve3,  1);
  //setIntegerParam(P_Valve4,  1);
  
// parameter inicializer
  setDoubleParam (P_Temperature0,       26.7);
  setDoubleParam (P_Temperature1,       36.7);
  setDoubleParam (P_Temperature2,       46.7);
  setDoubleParam (P_Temperature3,       56.7);
  setDoubleParam (P_Temperature4,       66.7);
  setDoubleParam (P_Temperature5,       76.7);
  setDoubleParam (P_Temperature6,       86.7);
  setDoubleParam (P_Temperature7,       96.7);

  setDoubleParam (P_Pressure1,       1013.0);
  setDoubleParam (P_Pressure2,       1013.0);
  setDoubleParam (P_Pressure3,       0.0);
  setDoubleParam (P_Pressure4,       0.0);

  setDoubleParam (P_Period0,       1);

  /* Create the thread that computes the waveforms in the background */
  status = (asynStatus)(epicsThreadCreate("serialPicAPDriverTask",
					  epicsThreadPriorityMedium,
					  epicsThreadGetStackSize(epicsThreadStackMedium),
					  (EPICSTHREADFUNC)::blockReadTask,
					  this) == NULL);
  if (status) {
    printf("%s:%s: epicsThreadCreate failure\n", driverName, functionName);
    return;
  }
}

void blockReadTask(void *drvPvt)
{
  serialPicAPDriver *pPvt = (serialPicAPDriver *)drvPvt;

  pPvt->blockReadTask();
}

/** Serial blocking read task to receive status data from dsPIC
 *
 *
 */

void serialPicAPDriver::blockReadTask(void)
{
  /* This thread process received data packages from dsPIC  and does callbacks with it */  
  char buf[BUFLEN];

  //int time =0;
  int readTimeout= 2;
  size_t nread;
  int eomReason;
  asynStatus status;
  asynUser *pasynUserSP = this->pasynUserSPort;

  int npar=0;
  int i;
  char tfld_strs[NPAR][PARMAX];
  char vfld_strs[NPAR][PARMAX];
  int pos = 0;
  /* Flush any stale input, since the next operation is likely to be a read */
  status = pasynOctetSyncIO->flush(pasynUserSP);

  while (1) {
    //  Clear buffer
    memset(&buf, 0, BUFLEN);
    status = pasynOctetSyncIO->read(pasynUserSP, buf, BUFLEN,
                                    readTimeout, &nread, &eomReason);
    if (status) {
      printf("%s: pasynOctetSyncIO->read failure,  eomReason:%d, status=%d\n", driverName, eomReason, status);
    }
    else{
      pos = 0;
      for ( i = 0; i < NPAR; i++){
        sscanf(buf + pos,"%[^_]_%[^ ]s", tfld_strs[i], vfld_strs[i]);
        //printf("%s : %s\n", tfld_strs[i], vfld_strs[i]);
        /*Begin read position of the buffer in next message*/
        pos = pos + strlen(tfld_strs[i]) + strlen(vfld_strs[i]) + 2;
        /*If at this position exists '\r' this means the end of message*/
        if (buf[pos + 3]=='\r') break;
      }
      npar = i + 1;
      //printf("\n\n%d : i = %d",npar,i);
      
      printf( "%s: pasynOctetSyncIO->read OK, nread:%d, eomReason:%d, status=%d, npars:%d\n",driverName, (int) nread, eomReason, status, npar);
      printf("%s\n",buf);
      //   for(i=0; i< 46 ; i++)
      //     printf("%X:%c ", buf[i], buf[i]);
      //   printf("\n");
      
      // Data decode
      for(i=0; i< npar; i++){
	    
        if (strcmp(vfld_strs[i], "ERR")!=0) {  
          
          /*****Valve*****
           *  MSG: VL1   */
          if (tfld_strs[i][0]=='V' && tfld_strs[i][1]=='L') {
            if      (tfld_strs[i][2]=='1' ) setIntegerParam(P_ValveState1, atoi(vfld_strs[i]));
            else if (tfld_strs[i][2]=='2' ) setIntegerParam(P_ValveState2, atoi(vfld_strs[i]));
            else if (tfld_strs[i][2]=='3' ) setIntegerParam(P_ValveState3, atoi(vfld_strs[i]));
            else if (tfld_strs[i][2]=='4' ) setIntegerParam(P_ValveState4, atoi(vfld_strs[i]));
          }

          /*****Temperature*****
           *  MSG: TE01         */
          else if (tfld_strs[i][0]=='T' && tfld_strs[i][1]=='E') {              
            if      (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='0' ) setDoubleParam(P_Temperature0, atof(vfld_strs[i]));
            else if (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='1' ) setDoubleParam(P_Temperature1, atof(vfld_strs[i]));
            else if (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='2' ) setDoubleParam(P_Temperature2, atof(vfld_strs[i]));
            else if (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='3' ) setDoubleParam(P_Temperature3, atof(vfld_strs[i]));
            else if (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='4' ) setDoubleParam(P_Temperature4, atof(vfld_strs[i]));
            else if (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='5' ) setDoubleParam(P_Temperature5, atof(vfld_strs[i]));
            else if (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='6' ) setDoubleParam(P_Temperature6, atof(vfld_strs[i]));
            else if (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='7' ) setDoubleParam(P_Temperature7, atof(vfld_strs[i]));
          }

          /*****Uptime*****
           *  MSG: UP     */
          else if (tfld_strs[i][0]=='U' && tfld_strs[i][1]=='P') 
            setIntegerParam(P_UpTime, atoi(vfld_strs[i]));
          
          /*****Pressure*****
           *  MSG: PR01     */
          else if (tfld_strs[i][0]=='P' && tfld_strs[i][1]=='R') {
              //tmpf =  atof(vfld_strs[i]) * 1e-20; // TODO conversion on the record             
            if      (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='1') setDoubleParam(P_Pressure1, atof(vfld_strs[i]) * 1e-20    );
            else if (tfld_strs[i][2]=='0' && tfld_strs[i][3]=='2') setDoubleParam(P_Pressure2, atof(vfld_strs[i]) * 1e-20    );         
          }
          /*****Pressure*****
           *  MSG: PRD01     */
          else if (tfld_strs[i][0]=='P' && tfld_strs[i][1]=='R' && tfld_strs[i][2]=='D') {
              //tmpf =  atof(vfld_strs[i]) * 1e-20; // TODO conversion on the record             
            if      (tfld_strs[i][3]=='0' && tfld_strs[i][4]=='1') setDoubleParam(P_Period0, atof(vfld_strs[i]) );    
          }
        }
      }
      //      printf("\n");
      //sscanf(buf,"%*[^U]UP_%d", &val); // fails if other codes contains U
      //      printf("uptime =%d\n", val);
      //setIntegerParam(P_UpTime, val);      
      //      sscanf(buf,"PR02_%*[^U]UP_%d", &val); // fails if other codes contains U

      callParamCallbacks();
    } 
    epicsThreadSleep(0.2);//POLL_DELAY give time for other serial I/O ops
  }
}

/** Called when asyn clients call pasynInt32->write().
 * This function sends a signal to the blockReadTask thread if the value of P_Run has changed.
 * For all parameters it sets the value in the parameter library and calls any registered callbacks..
 * \param[in] pasynUser pasynUser structure that encodes the reason and address.
 * \param[in] value Value to write. */
asynStatus serialPicAPDriver::writeInt32(asynUser *pasynUser, epicsInt32 value)
{
  int function = pasynUser->reason;
  asynStatus status = asynSuccess;
  asynUser *pasynUserSP = this->pasynUserSPort;

  const char *paramName;
  const char *functionName = "writeInt32";
  //  const char *VL1_str[]  = {"VL1_0\r", "VL1_1\r"};
  const char *VL1_str[]  = {"VL1_0\r\n", "VL1_1\r\n"};
  const char *VL2_str[]  = {"VL2_0\r\n", "VL2_1\r\n"};
  const char *VL3_str[]  = {"VL3_0\r\n", "VL3_1\r\n"};
  const char *VL4_str[]  = {"VL4_0\r\n", "VL4_1\r\n"};
  //const char *VL1_str[]  = {"VL1_0", "VL1_1"};

  size_t nwrite =0;
 
  /* Set the parameter in the parameter library. */
  status = (asynStatus) setIntegerParam(function, value);

  /* Fetch the parameter string name for possible use in debugging */
  getParamName(function, &paramName);

  if (function == P_ValveChange1) {
    // TODO check -1 < value < 2
    status = pasynOctetSyncIO->write(pasynUserSP, VL1_str[value], strlen(VL1_str[value]), 
				     WRITE_TIMEOUT, &nwrite);
    printf("OctetWrite:%d %s", (int) nwrite, VL1_str[value]); 
    //    printf("%d %2f %d\n", (int ) strlen(VL1_str[value]), WRITE_TIMEOUT, (int) nwrite);
    if (status) {
      printf("OctetWrite ERROR\n");
      asynPrint(pasynUser, ASYN_TRACE_ERROR,
		"echoListener: write buffer: %s: nwrite:%d %s\n",
                VL1_str[value], (int) nwrite, pasynUser->errorMessage);
       //      goto done;
    }
  }

  else if (function == P_ValveChange2) {
    // TODO check -1 < value < 2
    status = pasynOctetSyncIO->write(pasynUserSP, VL2_str[value], strlen(VL2_str[value]), 
                                     WRITE_TIMEOUT, &nwrite);
    printf("OctetWrite:%d %s", (int) nwrite, VL2_str[value]); 
    //    printf("%d %2f %d\n", (int ) strlen(VL1_str[value]), WRITE_TIMEOUT, (int) nwrite);
    if (status) {
      printf("OctetWrite ERROR\n");
      asynPrint(pasynUser, ASYN_TRACE_ERROR,
                "echoListener: write buffer: %s: nwrite:%d %s\n",
                VL2_str[value], (int) nwrite, pasynUser->errorMessage);
       //      goto done;
    }
  }

  else if (function == P_ValveChange3) {
    // TODO check -1 < value < 2
    status = pasynOctetSyncIO->write(pasynUserSP, VL3_str[value], strlen(VL3_str[value]), 
                                     WRITE_TIMEOUT, &nwrite);
    printf("OctetWrite:%d %s", (int) nwrite, VL3_str[value]); 
    //    printf("%d %2f %d\n", (int ) strlen(VL1_str[value]), WRITE_TIMEOUT, (int) nwrite);
    if (status) {
      printf("OctetWrite ERROR\n");
      asynPrint(pasynUser, ASYN_TRACE_ERROR,
                "echoListener: write buffer: %s: nwrite:%d %s\n",
                VL3_str[value], (int) nwrite, pasynUser->errorMessage);
       //      goto done;
    }
  }

  else if (function == P_ValveChange4) {
    // TODO check -1 < value < 2
    status = pasynOctetSyncIO->write(pasynUserSP, VL4_str[value], strlen(VL4_str[value]), 
                                     WRITE_TIMEOUT, &nwrite);
    printf("OctetWrite:%d %s", (int) nwrite, VL4_str[value]); 
    //    printf("%d %2f %d\n", (int ) strlen(VL1_str[value]), WRITE_TIMEOUT, (int) nwrite);
    if (status) {
      printf("OctetWrite ERROR\n");
      asynPrint(pasynUser, ASYN_TRACE_ERROR,
                "echoListener: write buffer: %s: nwrite:%d %s\n",
                VL4_str[value], (int) nwrite, pasynUser->errorMessage);
       //      goto done;
    }
  }
  // }
  // if (function == P_Run) {
  //   /* If run was set then wake up the simulation task */
  //   if (value) epicsEventSignal(eventId_);
  // }
  // else if (function == P_VertGainSelect) {
  //   setVertGain();
  // }
  // else if (function == P_VoltsPerDivSelect) {
  //   setVoltsPerDiv();
  // }
  // else if (function == P_TimePerDivSelect) {
  //   setTimePerDiv();
  // }
  // else {
  //   /* All other parameters just get set in parameter list, no need to
  //    * act on them here */
  // }

  /* Do callbacks so higher layers see any changes */
  status = (asynStatus) callParamCallbacks();

  if (status)
    epicsSnprintf(pasynUser->errorMessage, pasynUser->errorMessageSize,
		  "%s:%s: status=%d, function=%d, name=%s, value=%d",
		  driverName, functionName, status, function, paramName, value);
  else
    asynPrint(pasynUser, ASYN_TRACEIO_DRIVER,
	      "%s:%s: function=%d, name=%s, value=%d\n",
	      driverName, functionName, function, paramName, value);
  return status;
}

/** Called when asyn clients call pasynFloat64->write().
 * This function 
 * For all  parameters it  sets the value in the parameter library and calls any registered callbacks.
 * \param[in] pasynUser pasynUser structure that encodes the reason and address.
 * \param[in] value Value to write. */
asynStatus serialPicAPDriver::writeFloat64(asynUser *pasynUser, epicsFloat64 value)
{
  int function = pasynUser->reason;
  asynStatus status = asynSuccess;
  //int run;
  const char *paramName;
  //const char* functionName = "writeFloat64";

  /* Set the parameter in the parameter library. */
  // status = (asynStatus) setDoubleParam(function, value);

  /* Fetch the parameter string name for possible use in debugging */
  getParamName(function, &paramName);
  return status;
}

/* Configuration routine.  Called directly, or from the iocsh function below */

extern "C" {

  /** EPICS iocsh callable function to call constructor for the serialPicAPDriver class.
   * \param[in] portName The name of the asyn port driver to be created.
   * \param[in] maxChars The maximum  number of  */
  int serialPicAPDriverConfigure(const char *portName, const char *serialPortName, int maxChars)
  {
    new serialPicAPDriver(portName, serialPortName, maxChars);
    return(asynSuccess);
  }

  /* EPICS iocsh shell commands */

  static const iocshArg initArg0 = { "portName",      iocshArgString};
  static const iocshArg initArg1 = { "serialPortName",iocshArgString};
  static const iocshArg initArg2 = { "max points",    iocshArgInt};
  static const iocshArg * const initArgs[] = {&initArg0, &initArg1, &initArg2};
  static const iocshFuncDef initFuncDef = {"serialPicAPDriverConfigure",3,initArgs};
  static void initCallFunc(const iocshArgBuf *args)
  {
    serialPicAPDriverConfigure(args[0].sval, args[1].sval, args[2].ival);
  }

  void serialPicAPDriverRegister(void)
  {
    iocshRegister(&initFuncDef,initCallFunc);
  }

  epicsExportRegistrar(serialPicAPDriverRegister);

}

