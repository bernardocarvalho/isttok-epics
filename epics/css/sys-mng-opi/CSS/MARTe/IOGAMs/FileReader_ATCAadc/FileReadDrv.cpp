/*
 * Copyright 2011 EFDA | European Fusion Development Agreement
 *
 * Licensed under the EUPL, Version 1.1 or - as soon they 
   will be approved by the European Commission - subsequent  
   versions of the EUPL (the "Licence"); 
 * You may not use this work except in compliance with the 
   Licence. 
 * You may obtain a copy of the Licence at: 
 *  
 * http://ec.europa.eu/idabc/eupl
 *
 * Unless required by applicable law or agreed to in 
   writing, software distributed under the Licence is 
   distributed on an "AS IS" basis, 
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
   express or implied. 
 * See the Licence for the specific language governing 
   permissions and limitations under the Licence. 
 *
 * $Id: FileReadDrv.cpp 3 2012-01-15 16:26:07Z aneto $
 *
**/

#include "FileReadDrv.h"
#include "GlobalObjectDataBase.h"

bool FileReadDrv::ObjectLoadSetup(ConfigurationDataBase &info,StreamInterface *err){
    AssertErrorCondition(Information, "FileReadDrv::ObjectLoadSetup: %s Loading signals", Name());

	printf("1\n");

    CDBExtended cdb(info);
    if(!GenericAcqModule::ObjectLoadSetup(info,err)){
        AssertErrorCondition(InitialisationError,"FileReadDrv::ObjectLoadSetup: %s GenericAcqModule::ObjectLoadSetup Failed",Name());
        return False;
    }

	printf("2\n");
    if(!cdb.ReadFString(fileName, "TimeFileName")){
        AssertErrorCondition(InitialisationError,"Initialise::ObjectLoadSetup: %s TimeFileName must be specified.",Name());
        return False;
    }	
	
    if(!f.OpenRead(fileName.Buffer())){
        AssertErrorCondition(InitialisationError,"Initialise::ObjectLoadSetup: %s failed to open file: %s", Name(), fileName.Buffer());
        return False;
    }

	uint32 fileSize = f.Size();

    numberOfSignalLists = Size();

    if(numberOfSignalLists < 1){
		AssertErrorCondition(InitialisationError,"FileReadDrv::ObjectLoadSetup: %s at least 1 FileSignalList must be specified.",Name());
		return False;
  	}

/*
    if(numberOfSignalLists != 1){

	    if(numberOfSignalLists > 1){
		AssertErrorCondition(InitialisationError,"FileReadDrv::ObjectLoadSetup: %s only 1 FileSignalList must be specified.",Name());
		return False;
	    }else{
		AssertErrorCondition(InitialisationError,"FileReadDrv::ObjectLoadSetup: %s at least 1 FileSignalList must be specified.",Name());
		return False;
    	    }
    }
*/

	printf("Before new\n");

    signalLists = new FileSignalList*[numberOfSignalLists];
    if(signalLists == NULL){
        AssertErrorCondition(InitialisationError,"FileReadDrv::ObjectLoadSetup: %s failed to allocate %d pointer for FileSignalList.",Name(), numberOfSignalLists);
        return False;
    }

	printf("Before for\n");
    int32 i=0;
    for(i=0; i<numberOfSignalLists; i++){
		printf("In for\n");
        signalLists[i] = (FileSignalList *)Find(i).operator->();
    }

	printf("After for\n");

    return True;
}

/**
 * GetData
 */
int32 FileReadDrv::GetData(uint32 usecTime, int32 *ibuffer, int32 bufferNumber){
    int32 i      = 0;
    char *buffer = (char *)ibuffer;

    cycleNumber++;

    for(i=0; i<numberOfSignalLists; i++){
	//signalLists[i]->LoadData();
        void *samples = signalLists[i]->GetNextSample(usecTime, cycleNumber);

        if(samples != NULL){
			//if (cycleNumber == 1){
//			printf("signalLists[%d]->signalType.ByteSize() = %d, NumberOfInputs() = %d,sample = %f\n", i, signalLists[i]->signalType.ByteSize(), NumberOfInputs(), *((float *) samples));
//			printf("signalLists[%d]->signalType.ByteSize() = %d, NumberOfInputs() = %d,sample = %d\n", i, signalLists[i]->signalType.ByteSize(), NumberOfInputs(), *((unsigned int *) samples));

			//}
            memcpy(buffer, samples, signalLists[i]->signalType.ByteSize());
//            buffer += signalLists[i]->signalType.ByteSize() * signalLists[i]->numberOfSignals * NumberOfInputs();
            buffer += signalLists[i]->signalType.ByteSize() * signalLists[i]->numberOfSignals;
        }
    }
    return 1;
}

OBJECTLOADREGISTER(FileReadDrv,"$Id: FileReadDrv.cpp 3 2012-01-15 16:26:07Z aneto $")

