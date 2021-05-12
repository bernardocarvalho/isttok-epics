#!../../bin/linux-arm/ISTTOKrpi

## You may have to change ISTTOKrpi to something else
## everywhere it appears in this file

< envPaths
epicsEnvSet( "STREAM_PROTOCOL_PATH", "$(TOP)/db" )
epicsEnvSet( "SAVE_DIR", "$(TOP)/iocBoot/$(IOC)" )
epicsEnvSet( "EPICS_CA_ADDR_LIST", "localhost 192.168.1.120 192.168.1.152")

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/ISTTOKrpi.dbd"
ISTTOKrpi_registerRecordDeviceDriver pdbbase

## Load  I2C drivers
drvAsynI2CConfigure( "I2C", "/dev/i2c-1", 1 )

## Load record instances
dbLoadRecords("db/ISTTOKstates.db","P=ISTTOK:,R=central:")
dbLoadRecords("db/ISTTOKpcf8574.db","P=ISTTOK:,R=central:,BUS=I2C")
dbLoadRecords("db/ISTTOKpcf8591.db","P=ISTTOK:,R=central:,BUS=I2C")
#dbLoadRecords("db/ISTTOKtda8444.db","P=ISTTOK:,R=central:,BUS=I2C")
dbLoadRecords("db/ISTTOKmachineControl.db","P=ISTTOK:,R=central:")

## Load Serial drivers
#drvAsynSerialPortConfigure("RS0","/dev/ttyUSB0")
#drvAsynSerialPortConfigure("RS0","/dev/ttyAMA0")

#asynSetOption("RS0", 0, "baud", "9600")
#asynSetOption("RS0", 0, "bits", "8")
#asynSetOption("RS0", 0, "parity", "none")
#asynSetOption("RS0", 0, "stop", "1")
#asynSetOption("RS0", 0, "clocal", "Y")
#asynSetOption("RS0", 0, "crtscts", "N")

# Pfeiffer sensor are connectoed to other RPI /(192.168.1.120)
#dbLoadRecords("db/ISTTOKpfeiffer.db","P=ISTTOK:,R=central:,bus=RS0")

# connect to the MAIL server mail.ipfn.tecnico.ulisboa.pt
#		,priority,noAutoConnect,noProcessEos
drvAsynIPPortConfigure("L0","193.136.136.3:25",0,1,0)

dbLoadRecords("db/sendmail.db", "P=ISTTOK:,PORT=L0,R=central:,L=0,A=0")

# Uncomment to Debug STREAMDEVICE serial activity
#var streamError 1
#var streamDebug 1
streamSetLogfile("logfile.txt")

## Run this to trace the stages of iocInit
#traceIocInit

#save_restoreSet_status_prefix("$(IOC):")
save_restoreSet_status_prefix("ISTTOK:")
set_requestfile_path("$(SAVE_DIR)")
set_savefile_path("$(SAVE_DIR)/save")
save_restoreSet_NumSeqFiles(3)
save_restoreSet_SeqPeriodInSeconds(600)
set_pass0_restoreFile("$(IOC).sav")
set_pass1_restoreFile("$(IOC).sav")
dbLoadRecords("$(AUTOSAVE)/asApp/Db/save_restoreStatus.db", "P=ISTTOK:")

cd "${TOP}/iocBoot/${IOC}"

asSetFilename("${TOP}/iocBoot/${IOC}/access_security.acf")

iocInit

#asInit

# Create request file and start periodic 'save’
# makeAutosaveFileFromDbInfo("$(SAVE_DIR)/$(IOC).req", "autosaveFields")
create_monitor_set("$(IOC).req", 30)

## Start any sequence programs , use safe mode
seq  IsttokSeqExec
