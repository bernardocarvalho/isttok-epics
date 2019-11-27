/*************************************************************************
 *
 * Project       : ISTTOK slow Control
 *
 * Description   : serialPicAPDriverApp.cpp
 *              based on testAsynPortDriver.cpp
 *
 * Author        : Bernardo Carvalho (IPFN-IST)
 *
 * Copyright (c) : (IPFN-IST)
 * Created 25-Feb-2013
 *
 * SVN keywords
 * $Date: 2014-08-17 18:30:17 +0100 (Sun, 17 Aug 2014) $
 * $Revision: 6572 $
 * $URL: http://metis.ipfn.ist.utl.pt:8888/svn/cdaq/ISTTOK/Software/EPICS/ISTTOKcontrol/branches/quintal/ISTTOKApp/src/serialPicAPDriver.h $
 *
 *
 ************************************************************************/

#include "asynPortDriver.h"


/* These are the drvInfo strings that are used to identify the parameters.
 * They are used by asyn clients, including standard asyn device support */

// Input Value from dsPIC tell us the UPTIME
#define P_UpTimeString            "PIC_UPTIME"          /* asynInt32,    r/o */

// Two values one to chage the valve state, the output  
// and one other to verify valve state, input type
#define P_ValveChange1String      "PIC_VALVE_CHANGE_1"  /* asynInt32,    r/w */
#define P_ValveState1String       "PIC_VALVE_STATE_1"   /* asynInt32,    r/o */
#define P_ValveChange2String      "PIC_VALVE_CHANGE_2"  /* asynInt32,    r/w */
#define P_ValveState2String       "PIC_VALVE_STATE_2"   /* asynInt32,    r/o */
#define P_ValveChange3String      "PIC_VALVE_CHANGE_3"  /* asynInt32,    r/w */
#define P_ValveState3String       "PIC_VALVE_STATE_3"   /* asynInt32,    r/o */
#define P_ValveChange4String      "PIC_VALVE_CHANGE_4"  /* asynInt32,    r/w */
#define P_ValveState4String       "PIC_VALVE_STATE_4"   /* asynInt32,    r/o */

// Input type to recive temperature data
#define P_Temperature0String      "PIC_TEMP_0_VAL"      /* asynFloat64,  r/o */
#define P_Temperature1String      "PIC_TEMP_1_VAL"      /* asynFloat64,  r/o */
#define P_Temperature2String      "PIC_TEMP_2_VAL"      /* asynFloat64,  r/o */
#define P_Temperature3String      "PIC_TEMP_3_VAL"      /* asynFloat64,  r/o */
#define P_Temperature4String      "PIC_TEMP_4_VAL"      /* asynFloat64,  r/o */
#define P_Temperature5String      "PIC_TEMP_5_VAL"      /* asynFloat64,  r/o */
#define P_Temperature6String      "PIC_TEMP_6_VAL"      /* asynFloat64,  r/o */
#define P_Temperature7String      "PIC_TEMP_7_VAL"      /* asynFloat64,  r/o */

// Input type to recive pressure data
#define P_Pressure1String         "PIC_PRESS_1_VAL"      /* asynFloat64,  r/o */
#define P_Pressure2String         "PIC_PRESS_2_VAL"      /* asynFloat64,  r/o */
#define P_Pressure3String         "PIC_PRESS_3_VAL"      /* asynFloat64,  r/o */
#define P_Pressure4String         "PIC_PRESS_4_VAL"      /* asynFloat64,  r/o */
#define P_Pressure5String         "PIC_PRESS_5_VAL"      /* asynFloat64,  r/o */

// Input type to receive priode
#define P_Period0String           "PIC_PERIOD_0_VAL"     /* asynFloat64,  r/o */


#define P_PulseNumberString       "PIC_PULSE_NUMBER"    /* asynInt32,    r/w */

//#define P_TimeBaseString          "PIC_TIME_BASE"      /* asynFloat64Array,  r/o */

/** Class that demonstrates the use of the asynPortDriver base class to greatly simplify the task
 * of writing an asyn port driver.
 * This class does a simple simulation of a digital oscilloscope.  It computes a waveform, computes
 * statistics on the waveform, and does callbacks with the statistics and the waveform data itself.
 * I have made the methods of this class public in order to generate doxygen documentation for them,
 * but they should really all be private. */
class serialPicAPDriver : public asynPortDriver {
 public:
  serialPicAPDriver(const char *portName, const char *serialportName, int maxArraySize);

  /* These are the methods that we override from asynPortDriver */
  virtual asynStatus writeInt32(asynUser *pasynUser, epicsInt32 value);
  virtual asynStatus writeFloat64(asynUser *pasynUser, epicsFloat64 value);
  //virtual asynStatus readFloat64Array(asynUser *pasynUser, epicsFloat64 *value,
  //				      size_t nElements, size_t *nIn);
  //virtual asynStatus readEnum(asynUser *pasynUser, char *strings[], int values[], int severities[],
  //			      size_t nElements, size_t *nIn);

  /* These are the methods that are new to this class */
  void blockReadTask(void);

 protected:
  /** Values used for pasynUser->reason, and indexes into the parameter library. */
  int P_UpTime;
  #define FIRST_PIC_COMMAND P_UpTime
  int P_ValveChange1,P_ValveState1,P_ValveChange2,P_ValveState2,P_ValveChange3,P_ValveState3,P_ValveChange4,P_ValveState4;
  int P_Temperature0, P_Temperature1, P_Temperature2, P_Temperature3, P_Temperature4, P_Temperature5, P_Temperature6, P_Temperature7;
  int P_Pressure1, P_Pressure2, P_Pressure3, P_Pressure4;
  int P_Period0;
  int P_PulseNumber;
  #define LAST_PIC_COMMAND P_PulseNumber

 private:
  /* Our data */
  epicsEventId eventId_;
  asynUser *pasynUserSPort;
  //  const char *outputString_;
//  epicsFloat64 *pData_;
  /* epicsFloat64 *pTimeBase_; */
  /* // Actual volts per division are these values divided by vertical gain */
  /* char *voltsPerDivStrings_[NUM_VERT_SELECTIONS]; */
  /* int voltsPerDivValues_[NUM_VERT_SELECTIONS]; */
  /* int voltsPerDivSeverities_[NUM_VERT_SELECTIONS]; */
  /* void setVertGain(); */
  /* void setVoltsPerDiv(); */
  /* void setTimePerDiv(); */
};


#define NUM_PIC_PARAMS (&LAST_PIC_COMMAND - &FIRST_PIC_COMMAND + 1)

