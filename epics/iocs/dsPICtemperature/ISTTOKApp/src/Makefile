TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC support library

LIBRARY_IOC += ISTTOKSupport

# Compile and add the code to the support library
ISTTOKSupport_SRCS += serialPicAPDriver.cpp

ISTTOKSupport_LIBS += asyn
ISTTOKSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

#=============================
# Build the IOC application

PROD_IOC = ISTTOK
# ISTTOK.dbd will be created and installed
DBD += ISTTOK.dbd

# ISTTOK.dbd will be made up from these files:
ISTTOK_DBD += base.dbd

# Include dbd files from all support applications:
#
ISTTOK_DBD += ISTTOKSupport.dbd

# Add all the support libraries needed by this IOC
ISTTOK_LIBS += ISTTOKSupport asyn

# ISTTOK_registerRecordDeviceDriver.cpp derives from ISTTOK.dbd
ISTTOK_SRCS += ISTTOK_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
ISTTOK_SRCS_DEFAULT += ISTTOKMain.cpp
ISTTOK_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#ISTTOK_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file

ifneq ($(SNCSEQ),)
    # Build sncExample into ISTTOKSupport
    # IsttokSequenceExecution_SNCFLAGS += +r
    # ISTTOK_DBD += IsttokSequenceExecution.dbd
    # ISTTOKSupport_SRCS += IsttokSequenceExecution.stt
    # ISTTOKSupport_LIBS += seq pv
    # ISTTOK_LIBS += seq pv
    # Build sncExample into ISTTOKSupport
    IsttokSeqExec_SNCFLAGS += +r
    ISTTOK_DBD += IsttokSeqExec.dbd
    ISTTOKSupport_SRCS += IsttokSeqExec.stt
    ISTTOKSupport_LIBS += seq pv
    ISTTOK_LIBS += seq pv

    # sncExample_SNCFLAGS += +r
    # ISTTOK_DBD += sncExample.dbd
    # ISTTOKSupport_SRCS += sncExample.stt
    # ISTTOKSupport_LIBS += seq pv
    # ISTTOK_LIBS += seq pv

endif

# Finally link to the EPICS Base libraries
ISTTOK_LIBS += $(EPICS_BASE_IOC_LIBS)


#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

