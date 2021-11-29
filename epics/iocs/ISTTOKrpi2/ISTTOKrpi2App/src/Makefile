TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = ISTTOKrpi2
# ISTTOKrpi2.dbd will be created and installed
DBD += ISTTOKrpi2.dbd

# ISTTOKrpi2.dbd will be made up from these files:
ISTTOKrpi2_DBD += base.dbd

# Include dbd files from all support applications:
#ISTTOKrpi2_DBD += xxx.dbd
ISTTOKrpi2_DBD += asyn.dbd
ISTTOKrpi2_DBD += stream.dbd
ISTTOKrpi2_DBD += drvAsynSerialPort.dbd
ISTTOKrpi2_DBD += asSupport.dbd

# Add all the support libraries needed by this IOC
#ISTTOKrpi2_LIBS += xxx
ISTTOKrpi2_LIBS += asyn
ISTTOKrpi2_LIBS += stream
ISTTOKrpi2_LIBS += autosave

# ISTTOKrpi2_registerRecordDeviceDriver.cpp derives from ISTTOKrpi2.dbd
ISTTOKrpi2_SRCS += ISTTOKrpi2_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
ISTTOKrpi2_SRCS_DEFAULT += ISTTOKrpi2Main.cpp
ISTTOKrpi2_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#ISTTOKrpi2_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
ISTTOKrpi2_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

