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
 * $Id: FileSignalList.cpp 3 2012-01-15 16:26:07Z aneto $
 *
**/

#include "FileSignalList.h"
#include "File.h"

bool FileSignalList::LoadData(){
    //Open the file

/*
    float*aux = (float*)data;
    for(int i=0;i<signalArraySize;i++){

	printf("Load data[%d]=%lf\n", i, aux[i]);
    }
*/
    return True;
}

bool FileSignalList::ObjectLoadSetup(ConfigurationDataBase &info,StreamInterface *err){
    GCNamedObject::ObjectLoadSetup(info, err);
	
	printf("Loading Signal\n");
    AssertErrorCondition(Information, "FileSignalList::ObjectLoadSetup: %s Loading signals", Name());

    CDBExtended cdb(info);

    if(!cdb.ReadFString(fileName, "FileName", "signal_vector")){
        AssertErrorCondition(InitialisationError,"FileReadDrv::ObjectLoadSetup: %s FileBaseName must be specified.",Name());
        return False;
    }

    //Read the data type
    FString signalTypeStr;
    if(!cdb.ReadFString(signalTypeStr, "SignalType", "float")){
        AssertErrorCondition(Warning, "FileSignalList::ObjectLoadSetup: %s did not specify SignalType. Assuming %s", Name(), signalTypeStr.Buffer());
    }

    if(!BTConvertFromString(signalType, signalTypeStr.Buffer())){
        AssertErrorCondition(InitialisationError,"FileSignalList::ObjectLoadSetup: %s failed to convert to signalType %s", Name(), signalTypeStr.Buffer());
        return False;
    }

    //Configure whatever is required to access the shared memory
    if(!cdb.ReadInt32(signalArraySize, "SignalArraySize", 100)){
        AssertErrorCondition(Warning,"DCSSignal::ObjectLoadSetup: %s SignalArraySize was not specified. using Default at 1.",Name());
    }

	numberOfSignals = signalArraySize;


    if(!f.OpenRead(fileName.Buffer())){
        AssertErrorCondition(InitialisationError,"Initialise::ObjectLoadSetup: %s failed to open file: %s", Name(), fileName.Buffer());
        return False;
    }

	uint32 fileSize = f.Size();

    if(fileSize != dataSize){
        AssertErrorCondition(Warning,"Initialise::ObjectLoadSetup: %s size [%d] is diferent from configured %d", Name(), fileSize, dataSize);
        //return False;
    }

	dataSize = fileSize;

	unsigned char * fileData = (unsigned char *) calloc(fileSize, sizeof(unsigned char));
	if (!fileData)
	{
		AssertErrorCondition(InitialisationError,"%s::Initialise: Not enough memory for file_data with size %zu", Name(), dataSize);
       	return False;
    }
	else
	{
		AssertErrorCondition(Information,"%s::Initialise: Memory allocated for file_data: %zu bytes", Name(), dataSize);	
	}

	signalData = (unsigned char *) calloc(fileSize, sizeof(unsigned char));
	if (!signalData)
	{
		AssertErrorCondition(InitialisationError,"%s::Initialise: Not enough memory for file_data with size %zu", Name(), dataSize);
       	return False;
    }
	else
	{
		AssertErrorCondition(Information,"%s::Initialise: Memory allocated for file_data: %zu bytes", Name(), dataSize);	
	}

//	printf("reading file %s\n", fileName.Buffer());
	f.Seek(SEEK_SET); 
	bool k = f.Read(fileData, fileSize);

    if(k == 0){
        AssertErrorCondition(InitialisationError,"Initialise::ObjectLoadSetup: %s failed read data from file: %s", Name(), fileName.Buffer());
        return False;
    }

/*
	for(int i=0; i<24; i++){
		printf("i = %d, data = %d, 0x%X\n", i, ((unsigned char *) fileData)[i], ((unsigned char *) fileData)[i]);
	}
*/
/*
	unsigned int result = ((unsigned char *) fileData)[0];
	result = (result << 8) | ((unsigned char *) fileData)[1];
	result = (result << 8) | ((unsigned char *) fileData)[2];
	result = (result << 8) | ((unsigned char *) fileData)[3];
	
	printf("first time = %x\n", ((unsigned int *) fileData)[0]);
	printf("first time = %d\n", ((unsigned int *) fileData)[0]);

	printf("first time corrected = %d, 0x%X\n", result);

	printf("sizeof(char) = %d\n", sizeof(char));
*/
	for(int i=0; i<=fileSize - sizeof(char)*4; i=i+sizeof(char)*4){
		((unsigned char *) signalData)[i+0] = fileData[i+3];
		((unsigned char *) signalData)[i+1] = fileData[i+2];
		((unsigned char *) signalData)[i+2] = fileData[i+1];
		((unsigned char *) signalData)[i+3] = fileData[i+0];
	}

//	printf("first value corrected = %d, 0x%X\n", ((unsigned int *) signalData)[0], ((unsigned int *) signalData)[0]);
//	printf("first value addr = 0x%X\n", ((unsigned int *) signalData));

	if(fileData != NULL)
	    free((void *&)fileData);

    return True;
}

void *FileSignalList::GetNextSample(uint32 usecTime, uint32 cycleNumber){

	int index = 0;

    if(signalData == NULL){
        AssertErrorCondition(FatalError,"FileSignalList::GetNextSample: %s Data is not ready or is NULL", Name()); 
        return NULL;
    }

	//circular buffer
	index = (cycleNumber-1)%(dataSize/signalType.ByteSize());

    //Moves the internal counter to the next sample after the specified time
    //and returns the previous sample
	/*
    while(time[sampleCounter] <= usecTime){
        sampleCounter++;
        if(sampleCounter == numberOfSamples){
            break;
        }
    }
	
    sampleCounter--;

    return (sampleCounter == -1) ? data : ((char *) data) + sampleCounter * (numberOfSignals *  signalType.ByteSize());
*/
	//return  ((char *) signalData);

//	printf("cycleNumber = %d, index = %d\n", cycleNumber, index);
//	printf("numberOfSignals = %d, signalType.ByteSize() = %d\n", numberOfSignals, signalType.ByteSize());

//	printf("index = %d\n", index);

//	if (index < 10){
/*
	printf("cycleNumber = %d, index = %d, dataSize = %d\n", cycleNumber, index, dataSize);
	printf("numberOfSignals = %d, signalType.ByteSize() = %d\n", numberOfSignals, signalType.ByteSize());
	printf("sample = %d\n", ((unsigned int *) signalData)[index]);
*/
//}

/*
	if (index == 0){
		printf("cycleNumber = %d, index = %d\n", cycleNumber, index);
		printf("numberOfSignals = %d, signalType.ByteSize() = %d\n", numberOfSignals, signalType.ByteSize());

		printf("sample = %d\n", *(((unsigned char *) signalData) + index * (numberOfSignals *  signalType.ByteSize())));

		printf("sample addr = 0x%X\n", (((unsigned char *) signalData) + index * (numberOfSignals *  signalType.ByteSize())));
	}
*/

    return  ((unsigned char *) signalData) + index * (numberOfSignals *  signalType.ByteSize());
}

OBJECTLOADREGISTER(FileSignalList,"$Id: FileSignalList.cpp 3 2012-01-15 16:26:07Z aneto $")

