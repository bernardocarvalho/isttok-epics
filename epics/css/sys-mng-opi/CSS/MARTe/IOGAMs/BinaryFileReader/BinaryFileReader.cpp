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
 * $Id: BinaryFileReader.cpp 3 2012-01-15 16:26:07Z aneto $
 *
**/

#include "BinaryFileReader.h"
#include "GlobalObjectDataBase.h"

bool BinaryFileReader::ObjectLoadSetup(ConfigurationDataBase &info,StreamInterface *err){
    AssertErrorCondition(Information, "BinaryFileReader::ObjectLoadSetup: %s Loading signals", Name());

    CDBExtended cdb(info);
              
    if(!GenericAcqModule::ObjectLoadSetup(info,err)){
        AssertErrorCondition(InitialisationError,"BinaryFileReader::ObjectLoadSetup: %s GenericAcqModule::ObjectLoadSetup Failed",Name());
        return False;
    }

	numberOfInputs = NumberOfInputs();

    printf("NumberOfInputs() = %d\n", numberOfInputs);

    
    
	if(!cdb.ReadUint32(dataSize, "DataSize")){
		AssertErrorCondition(InitialisationError,"%s %s::Initialise: data_size is not specified.", IOGAM_MODULE, Name());
		return False;
	}
	
	AssertErrorCondition(Information,"%s %s::Initialise: data_size: %d", IOGAM_MODULE, Name(), dataSize);

	if(dataSize%sizeof(uint32) != 0){
		AssertErrorCondition(InitialisationError,"%s %s::Initialise: data_size is not valid. Must be a %zu multiple.", IOGAM_MODULE, Name(), sizeof(uint32));
		return False;
	}
	
	printf("memory alloc (sizeof(uint32)*numberOfInputs) = %zu\n", sizeof(uint32)*numberOfInputs);
	printf("memory alloc (sizeof(char)*dataSize) = %zu\n", sizeof(char)*dataSize);
	
	fileData = (char *) calloc(dataSize, sizeof(char));
	if (!fileData)
	{
		AssertErrorCondition(InitialisationError,"%s %s::Initialise: Not enough memory for file_data with size %zu", IOGAM_MODULE, Name(), dataSize);
        	return False;
    	}
	else
	{
		AssertErrorCondition(Information,"%s %s::Initialise: Memory allocated for file_data: %zu bytes", IOGAM_MODULE, Name(), dataSize);	
	}
    		
	
    if(!cdb.ReadFString(fileName, "FileName")){
        AssertErrorCondition(InitialisationError,"Initialise::ObjectLoadSetup: %s FilePath must be specified.",Name());
        return False;
    }	
	
    if(!f.OpenRead(fileName.Buffer())){
        AssertErrorCondition(InitialisationError,"Initialise::ObjectLoadSetup: %s failed to open file: %s", Name(), fileName.Buffer());
        return False;
    }

	uint32 fileSize = f.Size();

    if(fileSize != dataSize){
        AssertErrorCondition(InitialisationError,"Initialise::ObjectLoadSetup: %s size [%d] is diferent from configured %d", Name(), fileSize, dataSize);
        //return False;
    }

	f.Seek(SEEK_SET); 
	bool k = f.Read(fileData, fileSize);

    if(k == 0){
        AssertErrorCondition(InitialisationError,"Initialise::ObjectLoadSetup: %s failed read data from file: %s", Name(), fileName.Buffer());
        return False;
    }
	    
    return True;
}

/**
 * GetData
 */
int32 BinaryFileReader::GetData(uint32 usecTime, int32 *ibuffer, int32 bufferNumber){
    int32 i      = 0;
    char *buffer = (char *)ibuffer;
    int value = 1234;
    
    /*
	f.Seek(SEEK_SET);    	
	bool k = f.Read(fileData, dataSize);
*/
	
	memcpy(buffer, fileData, numberOfInputs*sizeof(char));    
	
    return 1;
}

OBJECTLOADREGISTER(BinaryFileReader,"$Id: BinaryFileReader.cpp 3 2012-01-15 16:26:07Z aneto $")
