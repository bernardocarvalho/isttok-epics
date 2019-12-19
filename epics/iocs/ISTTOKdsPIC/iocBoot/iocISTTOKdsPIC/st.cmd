#!../../bin/linux-x86_64/ISTTOKdsPIC

## You may have to change ISTTOKdsPIC to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet ("STREAM_PROTOCOL_PATH","$(TOP)/db")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/ISTTOKdsPIC.dbd"
ISTTOKdsPIC_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=codac-dev")
# Setup serial port 2
drvAsynSerialPortConfigure("COM2","/dev/ttyS2",0,0,0)
asynSetOption("COM2",  -1,  "baud",  "115200")
asynSetOption("COM2",  -1,  "bits",  "8")
asynSetOption("COM2",  -1,  "parity",  "none")
asynSetOption("COM2",  -1,  "stop",  "1")
asynSetOption("COM2",  -1,  "clocal",  "Y")
asynSetOption("COM2",  -1,  "crtscts",  "N")
#### Uncomment for ASYNS debuging ####
#asynSetTraceMask("COM2",  0, 9)
#asynSetTraceIOMask("COM2",0, 0x2)

## Setup support for dsPIC interface 2
dbLoadRecords("db/ISTTOKtemperature.db","P=ISTTOK:,R=temperature:,PORT=COM2,A=0")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=codac-dev"
