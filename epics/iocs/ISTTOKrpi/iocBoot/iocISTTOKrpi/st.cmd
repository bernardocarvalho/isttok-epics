#!../../bin/linux-arm/ISTTOKrpi

## You may have to change ISTTOKrpi to something else
## everywhere it appears in this file

< envPaths
epicsEnvSet( "STREAM_PROTOCOL_PATH", "$(TOP)/protocols" )
epicsEnvSet( "SAVE_DIR", "$(TOP)/iocBoot/$(IOC)" )
epicsEnvSet( "EPICS_CA_ADDR_LIST", "localhost 192.168.1.152")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/ISTTOKrpi.dbd"
ISTTOKrpi_registerRecordDeviceDriver pdbbase

## Load  I2C drivers
drvAsynI2CConfigure( "I2C", "/dev/i2c-1", 1 )

## Load record instances
dbLoadRecords("db/ISTTOKstates.db","P=ISTTOK:,R=central:")
dbLoadRecords("db/ISTTOKpcf8574.db","P=ISTTOK:,R=central:")
dbLoadRecords("db/ISTTOKpcf8591.db","P=ISTTOK:,R=central:")
dbLoadRecords("db/ISTTOKmachineControl.db","P=ISTTOK:,R=central:")

## Load Serial drivers
drvAsynSerialPortConfigure("RS0","/dev/ttyUSB0")

asynSetOption("RS0", 0, "baud", "9600")
asynSetOption("RS0", 0, "bits", "8")
asynSetOption("RS0", 0, "parity", "none")
asynSetOption("RS0", 0, "stop", "1")
asynSetOption("RS0", 0, "clocal", "Y")
asynSetOption("RS0", 0, "crtscts", "N")

dbLoadRecords("db/ISTTOKpfeiffer.db","P=ISTTOK:,R=central:,bus=RS0")

# Uncomment to Debug STREAM serial activity
#var streamError 1
#var streamDebug 1
#streamSetLogfile("logfile.txt")

## Run this to trace the stages of iocInit
#traceIocInit

#save_restoreSet_status_prefix("$(IOC):")
save_restoreSet_status_prefix("xxx:")
set_requestfile_path("$(SAVE_DIR)")
set_savefile_path("$(SAVE_DIR)/save")
save_restoreSet_NumSeqFiles(3)
save_restoreSet_SeqPeriodInSeconds(600)
set_pass2_restoreFile("$(IOC).sav")
set_pass1_restoreFile("$(IOC).sav")
dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=xxx:")

cd "${TOP}/iocBoot/${IOC}"

asSetFilename("${TOP}/iocBoot/${IOC}/access_security.acf")

iocInit

#asInit

# Create request file and start periodic 'save’
# makeAutosaveFileFromDbInfo("$(SAVE_DIR)/$(IOC).req", "autosaveFields")
create_monitor_set("$(IOC).req", 30)

## Start any sequence programs
seq IsttokSeqExec
#, "unit=ISTTOK"
