#!../../bin/linux-arm/ISTTOKrpi2

#- You may have to change ISTTOKrpi2 to something else
#- everywhere it appears in this file

< envPaths
epicsEnvSet( "STREAM_PROTOCOL_PATH", "$(TOP)/db" )
epicsEnvSet( "SAVE_DIR", "$(TOP)/iocBoot/$(IOC)" )

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
# Uncomment to Debug STREAM serial activity
#var streamError 1
#var streamDebug 1
#streamSetLogfile("stream_logfile.txt")

#save_restoreSet_status_prefix("$(IOC):")
save_restoreSet_status_prefix("ISTTOK:")
set_requestfile_path("$(SAVE_DIR)")
set_savefile_path("$(SAVE_DIR)/save")
save_restoreSet_NumSeqFiles(3)
save_restoreSet_SeqPeriodInSeconds(600)
set_pass0_restoreFile("$(IOC).sav")
set_pass1_restoreFile("$(IOC).sav")
#dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=ISTTOK:")
 
cd "${TOP}/iocBoot/${IOC}"
iocInit

# Create request file and start periodic 'save’
# makeAutosaveFileFromDbInfo("$(SAVE_DIR)/$(IOC).req", "autosaveFields")
create_monitor_set("$(IOC).req", 30)

## Start any sequence programs
#seq sncxxx,"user=pi"
