#!/home/oper/ISTTOK/epics/iocs/dsPICTemp/bin/linux-x86_64/ISTTOK

#- You may have to change ISTTOK to something else
#- everywhere it appears in this file

< envPaths

epicsEnvSet( "STREAM_PROTOCOL_PATH", "$(TOP)/db" )

epicsEnvSet( "EPICS_CA_ADDR_LIST", "localhost 192.168.1.120 192.168.1.110")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/ISTTOK.dbd"
ISTTOK_registerRecordDeviceDriver pdbbase

#drvAsynSerialPortConfigure("RS232","/dev/ttyUSB1")
drvAsynSerialPortConfigure("RS232","/dev/dsPIC0")
asynSetOption("RS232", 0, "baud", "115200")
asynSetOption("RS232", 0, "bits", "8")
asynSetOption("RS232", 0, "parity", "none")
asynSetOption("RS232", 0, "stop", "1")
#asynSetOption("RS232", 0, "clocal", "N")
#asynSetOption("RS232", 0, "crtscts", "Y")

## Load record instances
dbLoadRecords("db/ISTTOKtemperature.db","P=ISTTOK:,R=temperature:,PORT=RS232,A=0")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=oper"
