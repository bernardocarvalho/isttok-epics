TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = ISTTOK
# ISTTOK.dbd will be created and installed
DBD += ISTTOK.dbd

# ISTTOK.dbd will be made up from these files:
ISTTOK_DBD += base.dbd

# Include dbd files from all support applications:
#ISTTOK_DBD += xxx.dbd
ISTTOK_DBD += asyn.dbd
ISTTOK_DBD += drvAsynSerialPort.dbd
ISTTOK_DBD += calc.dbd
ISTTOK_DBD += stream.dbd

# Add all the support libraries needed by this IOC
#ISTTOK_LIBS += xxx
ISTTOK_LIBS += asyn
ISTTOK_LIBS += calc
ISTTOK_LIBS += stream

# ISTTOK_registerRecordDeviceDriver.cpp derives from ISTTOK.dbd
ISTTOK_SRCS += ISTTOK_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
ISTTOK_SRCS_DEFAULT += ISTTOKMain.cpp
ISTTOK_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#ISTTOK_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
ISTTOK_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

