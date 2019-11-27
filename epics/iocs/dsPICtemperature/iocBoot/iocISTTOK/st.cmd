#!../../bin/linux-x86_64/ISTTOK
#
# $Author: gquintal $
# $Id: st.cmd 6581 2014-08-20 16:03:44Z gquintal $
< envPaths

cd ${TOP}

## Register all support components
dbLoadDatabase "dbd/ISTTOK.dbd"
ISTTOK_registerRecordDeviceDriver pdbbase

## Setup serial port 0
drvAsynSerialPortConfigure("RS232","/dev/ttyS0",0,0,0)
asynSetOption("RS232",  -1,  "baud",  "115200")
asynSetOption("RS232",  -1,  "bits",  "8")
asynSetOption("RS232",  -1,  "parity",  "none")
asynSetOption("RS232",  -1,  "stop",  "1")
#modem control lines (Data Terminal Ready, Carrier Detect/Received Line Signal Detect) are used (clocal=N) or ignored (clocal=Y)
asynSetOption("RS232",  -1,  "clocal",  "Y")
asynSetOption("RS232",  -1,  "crtscts",  "N")

#### Uncomment for ASYNS debuging #### 
#asynSetTraceMask("RS232",  0, 9)
#asynSetTraceIOMask("RS232",0, 0x2)

## Setup support for dsPIC interface 0 
serialPicAPDriverConfigure("dsPIC", "RS232", 0)
dbLoadRecords("db/ISTTOKgalium.db","P=ISTTOK:,R=galium:,PORT=dsPIC,ADDR=0,TIMEOUT=1,NPOINTS=0")

## Setup serial port 3
drvAsynSerialPortConfigure("COM3","/dev/ttyS3",0,0,0)
asynSetOption("COM3",  -1,  "baud",  "115200")
asynSetOption("COM3",  -1,  "bits",  "8")
asynSetOption("COM3",  -1,  "parity",  "none")
asynSetOption("COM3",  -1,  "stop",  "1")
asynSetOption("COM3",  -1,  "clocal",  "Y")
asynSetOption("COM3",  -1,  "crtscts",  "N")
#### Uncomment for ASYNS debuging #### 
#asynSetTraceMask("COM3",  0, 9)
#asynSetTraceIOMask("COM3",0, 0x2)

## Setup support for dsPIC interface 1
serialPicAPDriverConfigure("dsPIC1", "COM3", 0)
dbLoadRecords("db/ISTTOKvacuum.db","P=ISTTOK:,R=vacuum:,PORT=dsPIC1,ADDR=0,TIMEOUT=1,NPOINTS=0")

## Setup serial port 2
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
serialPicAPDriverConfigure("dsPIC2", "COM2", 0)
dbLoadRecords("db/ISTTOKtemperature.db","P=ISTTOK:,R=temperature:,PORT=dsPIC2,ADDR=0,TIMEOUT=1,NPOINTS=0")

##### 
dbLoadRecords("db/ISTTOKcontrol.db","P=ISTTOK:,R=central:")

# IOCLogClient start:
iocLogInit()

iocInit()

## Start any sequence programs
#seq IsttokSequenceExecution,
seq IsttokSeqExec, "unit=ISTTOK"
