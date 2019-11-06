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
 * $Id: BinaryFileReader.h 3 2012-01-15 16:26:07Z aneto $
 *
**/

#if !defined (BINARY_FILE_READER)
#define BINARY_FILE_READER

#include "System.h"
#include "GenericAcqModule.h"
#include "File.h"
#include "ConfigurationDataBase.h"
#include "CDBExtended.h"

class DDBInputInterface;
class DDBOutputInterface;

#define IOGAM_MODULE "BinaryFileReader"

OBJECT_DLL(BinaryFileReader)
class BinaryFileReader: public GenericAcqModule{
OBJECT_DLL_STUFF(BinaryFileReader)

private:

    File f;
    /**
     * Cycle Number
    */
    int64 cycleNumber;
    uint32 dataSize;
    uint32 numberOfInputs;
    
    /** Output interface to write data to */
    DDBInputInterface                     *input;

    /**
     * Number of signals
    */
	uint32 numberOfSignals;

    /**
     * Double array with signals
    */
	char ** signals;
    /**
     * File Names. For each Channel
    */
    FString fileName_usecTime;
    FString fileName_Ch1;

    
public:
    BinaryFileReader(){
        cycleNumber = 0;
    }

    virtual ~BinaryFileReader(){
	delete [] fileData;
    }

    /**
     * Reset the internal counters 
     */
    bool PulseStart(){
        cycleNumber = 0;
        return True;
    }


    /** 
     * Gets Data From the Module to the DDB
     * @param usecTime Microseconds Time
     * @return -1 on Error, 1 on success
     */
    int32 GetData(uint32 usecTime, int32 *buffer, int32 bufferNumber = 0);

    /**
     * Load and configure object parameters
     * @param info the configuration database
     * @param err the error stream
     * @return True if no errors are found during object configuration
     */
    bool ObjectLoadSetup(ConfigurationDataBase &info,StreamInterface *err);

    /**
     * NOOP
     */
    bool ObjectDescription(StreamInterface &s,bool full,StreamInterface *er){
        return True;
    }

    /**
     * NOOP
     */
    bool SetInputBoardInUse(bool on){
        return True;
    }

    /**
     * NOOP
     */
    bool SetOutputBoardInUse(bool on){
        return True;
    }

    /**
     * Not supported
     */
    bool WriteData(uint32 usecTime, const int32* buffer){
        AssertErrorCondition(FatalError, "%s: WriteData not supported", Name());
        return False;
    }
};

#endif
