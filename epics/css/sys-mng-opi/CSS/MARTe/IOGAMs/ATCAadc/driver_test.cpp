//******************************************************************************
//    MARTe Library
//    $Log: driver_test.cpp,v $
//    Revision 1.17  2009/03/31 08:11:37  aneto
//    Support for multiple input
//
//    Revision 1.16  2009/01/26 09:20:38  aneto
//    linux support
//
//    Revision 1.15  2008/08/01 16:29:13  rvitelli
//    trigger
//
//    Revision 1.14  2008/08/01 14:09:26  rvitelli
//    First working version
//
//    Revision 1.13  2008/06/19 10:15:46  rvitelli
//    Lowered sleep between GetData calls to allow execution of LongSleeps. Probably a problem due to execution of mod_writer and driver_test on the same processor.
//
//    Revision 1.12  2008/06/19 07:22:49  rvitelli
//    Added std_dev
//
//    Revision 1.11  2008/06/18 17:19:04  rvitelli
//    Optimization.
//
//    Revision 1.10  2008/06/18 17:06:36  rvitelli
//    Added variance statistic.
//
//    Revision 1.9  2008/06/18 16:49:21  rvitelli
//    Minor bug.
//******************************************************************************

#include "Console.h"
#include "Sleep.h"
#include "ATCAadcDrv.h"
#include "Threads.h"
#include "LoggerService.h"
#include "File.h"
#include "SXMemory.h"
#include "ConfigurationDataBase.h"
#include "GCReferenceContainer.h"
#include "GlobalObjectDataBase.h"
#include "MenuContainer.h"
#include "ProcessorType.h"

const char *cdbMap=
"+ATCA_DRIVER={\n"
"    Class = ATCAadcDrv\n"
"    Title = \"ATCA Driver test\" \n"
"    SoftTrigger=1\n"
"    NumberOfOutputs=8\n"
"    NumberOfInputs=64\n"
"    ExtTriggerAndClock=1\n"
"}\n"
"+MENUS={"
"    Class = MenuContainer\n"
"    Title = \"ATCA ADC Driver Test\" \n"
"    +START_ACK_MENU={\n"
"        Class = MenuEntry\n"
"        Title = \"Start Acquisition\"\n"
"    }\n"
"    +STOP_ACK_MENU={\n"
"        Class = MenuEntry\n"
"        Title = \"Stop Acquisition\"\n"
"    }\n"
"    +SAVE_DATA_MENU={\n"
"        Class = MenuEntry\n"
"        Title = \"Save acquired data\"\n"
"    }\n"
"    +PRINT_DATA_MENU={\n"
"        Class = MenuEntry\n"
"        Title = \"Print last buffer\"\n"
"    }\n"
"}";

volatile int keepAlive     = 0;
int64 max_timer            = 0;
float mean_exec_time       = 0;
float meansquare_exec_time = 0;
float variance_exec_time   = 0;

const int32 BUFFER_BOARD_TRF_SIZE = 33 + 2 * HEADER_LENGTH;
const int32 MAX_SAMPLES_TO_SAVE   = 100;

int32 buffer[70];
uint32 outputBuffer[3];
uint32 dataBrd1[BUFFER_BOARD_TRF_SIZE * MAX_SAMPLES_TO_SAVE];
int32 dataBrd2[BUFFER_BOARD_TRF_SIZE * MAX_SAMPLES_TO_SAVE];

int32 printLastBuffer = 0;

GCRTemplate<GenericAcqModule> driver;

void __thread_decl acquisitionThread(void *ptr){
	int   k              = 0;
	int64 timer          = 0;
	int64 timer_after    = 0;
	int   ret            = 0;
	
	max_timer            = 0;
	mean_exec_time       = 0;
	meansquare_exec_time = 0;
	variance_exec_time   = 0;
	
	driver->EnableAcquisition();

	int triggerReceived = 0;
	memset(buffer, 0, BUFFER_BOARD_TRF_SIZE * sizeof(int32));
	memset(dataBrd1, 0, BUFFER_BOARD_TRF_SIZE * MAX_SAMPLES_TO_SAVE * sizeof(int32));
	memset(dataBrd2, 0, BUFFER_BOARD_TRF_SIZE * MAX_SAMPLES_TO_SAVE * sizeof(int32));
	//Console con;
	printf("Starting\n");
	while (keepAlive != 0){
		timer = HRT::HRTCounter();
		SleepSec(10E-6);
		ret = driver->GetData(0, buffer);

		printf("Time: [%d], k = %d, BUFFER_BOARD_TRF_SIZE = %d!\n", dataBrd1[0], k, BUFFER_BOARD_TRF_SIZE);
		printf("Time End = %d, Status = %d\n", dataBrd1[BUFFER_BOARD_TRF_SIZE - 1], dataBrd1[BUFFER_BOARD_TRF_SIZE - 2]);


		if(dataBrd1[0] == 0 && k > 5){
			triggerReceived      = 1;
			k                    = 0;
			max_timer            = 0;
			mean_exec_time       = 0;
			meansquare_exec_time = 0;
			variance_exec_time   = 0;
			printf("Trigger received!\n");

		}

		if(printLastBuffer > 0){
			printf("H[%d] = %d F[%d] = %d\n", k, 0, k, dataBrd1[BUFFER_BOARD_TRF_SIZE - 1]);
			printLastBuffer = 0;
		}

		if(triggerReceived == 1 && k < MAX_SAMPLES_TO_SAVE){
			for(int j=0; j<BUFFER_BOARD_TRF_SIZE; j++){
				dataBrd1[BUFFER_BOARD_TRF_SIZE * k + j] = buffer[j];
				dataBrd2[BUFFER_BOARD_TRF_SIZE * k + j] = buffer[BUFFER_BOARD_TRF_SIZE + j];
			}
			//dataBrd1[BUFFER_BOARD_TRF_SIZE * k] = ret * HRT::HRT::HRTPeriod() * 1000000;//buffer[0];
		}

		outputBuffer[0] = 0;
		outputBuffer[1] = 7;
		outputBuffer[2] += 10;
		driver->WriteData(0, (int32 *)outputBuffer);

		timer_after = HRT::HRTCounter();
		if ( (timer_after - timer) > max_timer) {
			max_timer = timer_after - timer;
		}
		mean_exec_time += (float)(timer_after - timer);
		meansquare_exec_time += (float)((timer_after - timer)*(timer_after - timer));
		k++;
	}
	driver->DisableAcquisition();
	mean_exec_time /= k;
	variance_exec_time = ( (meansquare_exec_time - max_timer*max_timer)/k - mean_exec_time*mean_exec_time); 
	keepAlive = 1;
}

bool StartAcquisition(StreamInterface &in,StreamInterface &out,void *userData){
	if(keepAlive != 0){
		out.Printf("Acquisition already started\n");
		return False;
	}
	keepAlive = 1;
	ProcessorType runCore(0x8);
	Threads::BeginThread(acquisitionThread, NULL, THREADS_DEFAULT_STACKSIZE, NULL, XH_NotHandled, runCore);
	return True;
}

bool StopAcquisition(StreamInterface &in,StreamInterface &out,void *userData){
        if(keepAlive == 0){
	        out.Printf("Acquisition already stopped\n");
		return False;
        }

	out.Printf("Stopping acquisition\n");
	keepAlive = 0;
	while(keepAlive != 1){
		SleepSec(1.0);
	}
	keepAlive = 0;
	out.Printf("Acquisition stopped\n");
	out.Printf("\nmax_timer = %f\n", max_timer*HRT::HRTPeriod()*1000000);
	out.Printf("mean_exec_time = %f\n", mean_exec_time*HRT::HRTPeriod()*1000000);
	out.Printf("dev_std_exec_time = %f\n", sqrt(variance_exec_time)*HRT::HRTPeriod()*1000000);
	out.Printf("max_error = %f\n", (max_timer-mean_exec_time)*HRT::HRTPeriod()*1000000);
}

bool SaveData(StreamInterface &in,StreamInterface &out,void *userData){
	out.Printf("Saving Data\n");
	File outputFile;
	FString dataDump;
	FString filename;
	FString dataDump2;
	dataDump.SetSize(BUFFER_BOARD_TRF_SIZE * MAX_SAMPLES_TO_SAVE);
	dataDump2.SetSize(BUFFER_BOARD_TRF_SIZE * MAX_SAMPLES_TO_SAVE);
	out.Printf("Printing in FString\n");
	for(int k=0; k<MAX_SAMPLES_TO_SAVE; k++){
		for(int j=0; j<BUFFER_BOARD_TRF_SIZE; j++){
			dataDump.Printf("%d ", dataBrd1[BUFFER_BOARD_TRF_SIZE * k + j]);
			dataDump2.Printf("%d ", dataBrd2[BUFFER_BOARD_TRF_SIZE * k + j]);
		}
		dataDump.Printf("\n");
		dataDump2.Printf("\n");
	}

	out.Printf("Printing in File\n");
	filename.Printf("data_%d.dump", time(NULL));
	outputFile.OpenNew(filename.Buffer());
	outputFile.Printf("%s", dataDump.Buffer());
	outputFile.Close();
	out.Printf("Data for board 1 saved at %s\n", filename.Buffer());
	filename.SetSize(0);
	filename.Printf("data2_%d.dump", time(NULL));
	outputFile.OpenNew(filename.Buffer());
	outputFile.Printf("%s", dataDump2.Buffer());	
	outputFile.Close();
	out.Printf("Data for board 2 saved at %s\n", filename.Buffer());
}

bool PrintLastBuffer(StreamInterface &in,StreamInterface &out,void *userData){
	printLastBuffer = 1;	
}

int main(int argc, char **argv) {
	
	LSSetUserAssembleErrorMessageFunction(LSAssembleErrorMessage);
	LSSetRemoteLogger("localhost",32767);
        LSStartService();

	SXMemory config((char *)cdbMap,strlen(cdbMap));
	ConfigurationDataBase cdb;
	if (!cdb->ReadFromStream(config,NULL)){
		CStaticAssertErrorCondition(ParametersError,"Init: cdb.ReadFromStream failed");
		return -1;
	}
	GCRTemplate<GCReferenceContainer> godb = GetGlobalObjectDataBase();
	godb->ObjectLoadSetup(cdb,NULL);

	GCRTemplate<MenuContainer> mc;
	mc = godb->Find("MENUS");
	if (!mc.IsValid()){
		CStaticAssertErrorCondition(FatalError,"cannot find MENUS MenuContainer object\n");
		return -2;
	}
	driver = godb->Find("ATCA_DRIVER");
	if (!driver.IsValid()){
		CStaticAssertErrorCondition(FatalError,"cannot find ATCA_DRIVER MenuContainer object\n");
		return -2;
	}
	Console con(PerformCharacterInput);
	con.SetPaging(True);

	mc->SetupItem("START_ACK_MENU", StartAcquisition, NULL, NULL, NULL);
	mc->SetupItem("STOP_ACK_MENU", StopAcquisition, NULL, NULL, NULL);
	mc->SetupItem("SAVE_DATA_MENU", SaveData, NULL, NULL, NULL);
	mc->SetupItem("PRINT_LAST_BUFFER", PrintLastBuffer, NULL, NULL, NULL);

	mc->TextMenu(con,con);
//	LSStopService();
	return 0;
}
