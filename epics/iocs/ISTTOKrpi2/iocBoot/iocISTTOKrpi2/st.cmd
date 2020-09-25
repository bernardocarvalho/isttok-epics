#!../../bin/linux-arm/ISTTOKrpi2

#- You may have to change ISTTOKrpi2 to something else
#- everywhere it appears in this file

< envPaths
epicsEnvSet( "STREAM_PROTOCOL_PATH", "$(TOP)/db" )

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/ISTTOKrpi2.dbd"
ISTTOKrpi2_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=pi")
## Load Serial drivers
drvAsynSerialPortConfigure("RS0","/dev/ttyUSB0")
#drvAsynSerialPortConfigure("RS0","/dev/ttyAMA0")

asynSetOption("RS0", 0, "baud", "9600")
asynSetOption("RS0", 0, "bits", "8")
asynSetOption("RS0", 0, "parity", "none")
asynSetOption("RS0", 0, "stop", "1")
asynSetOption("RS0", 0, "clocal", "Y")
asynSetOption("RS0", 0, "crtscts", "N")

dbLoadRecords("db/ISTTOKpfeiffer.db","P=ISTTOK:,R=vacuum:,bus=RS0")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=pi"
