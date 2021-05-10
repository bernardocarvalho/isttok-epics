TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS BELOW HERE

# Use typed rset structure (see 3.16.1 release notes)
USR_CPPFLAGS += -DUSE_TYPED_RSET

# xxxRecord.h will be created from xxxRecord.dbd
#DBDINC += xxxRecord

# Install xxxSupport.dbd into <top>/dbd
#DBD += xxxSupport.dbd

# Build an IOC support library
LIBRARY_IOC += ISTTOKrpiSupport

# Compile and add code to the support library
#ISTTOKrpiSupport_SRCS += xxxRecord.c
#ISTTOKrpiSupport_SRCS += devXxxSoft.c

# Link locally-provided code into the support library,
# rather than directly into the IOC application, that
# causes problems on Windows DLL builds
#ISTTOKrpiSupport_SRCS += dbSubExample.c
#ISTTOKrpiSupport_SRCS += devISTTOKrpiVersion.c
#ISTTOKrpiSupport_SRCS += ISTTOKrpiHello.c
ISTTOKrpiSupport_SRCS += initTrace.c

ISTTOKrpiSupport_LIBS += $(EPICS_BASE_IOC_LIBS)

# Auto-generate a header file containing a version string.
# Version comes from the VCS if available, else date+time.
#GENVERSION = ISTTOKrpiVersion.h
# Macro name
#GENVERSIONMACRO = ISTTOKrpiVERSION

# Build the IOC application
PROD_IOC = ISTTOKrpi

# ISTTOKrpi.dbd will be created and installed
DBD += ISTTOKrpi.dbd

# ISTTOKrpi.dbd will include these files:
ISTTOKrpi_DBD += base.dbd
ISTTOKrpi_DBD += initTrace.dbd
# Include dbd files from all support applications:
ISTTOKrpi_DBD += asyn.dbd
#ISTTOKrpi_DBD += calc.dbd
ISTTOKrpi_DBD += stream.dbd
ISTTOKrpi_DBD += drvAsynI2C.dbd
ISTTOKrpi_DBD += drvAsynSerialPort.dbd
ISTTOKrpi_DBD += drvAsynIPPort.dbd
ISTTOKrpi_DBD += asSupport.dbd

# Add all the support libraries needed by this IOC
ISTTOKrpi_LIBS += asyn
#ISTTOKrpi_LIBS += calc
ISTTOKrpi_LIBS += stream
ISTTOKrpi_LIBS += drvAsynI2C
ISTTOKrpi_LIBS += autosave

# ISTTOKrpi_registerRecordDeviceDriver.cpp derives from ISTTOKrpi.dbd
ISTTOKrpi_SRCS += ISTTOKrpi_registerRecordDeviceDriver.cpp

# Build the main IOC entry point where needed
ISTTOKrpi_SRCS_DEFAULT += ISTTOKrpiMain.cpp
ISTTOKrpi_SRCS_vxWorks += -nil-

# Link in the code from our support library
ISTTOKrpi_LIBS += ISTTOKrpiSupport

# To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
ifneq ($(SNCSEQ),)
    # Build sncExample into ISTTOKrpiSupport , Safe Mode : +s
    IsttokSeqExec_SNCFLAGS += +r +s
    ISTTOKrpi_DBD += IsttokSeqExec.dbd
    # A .stt sequence program is *not* pre-processed:
    ISTTOKrpiSupport_SRCS += IsttokSeqExec.stt
    ISTTOKrpiSupport_LIBS += seq pv
    ISTTOKrpi_LIBS += seq pv
endif

# Link QSRV (pvAccess Server) if available
ifdef EPICS_QSRV_MAJOR_VERSION
    ISTTOKrpi_LIBS += qsrv
    ISTTOKrpi_LIBS += $(EPICS_BASE_PVA_CORE_LIBS)
    ISTTOKrpi_DBD += PVAServerRegister.dbd
    ISTTOKrpi_DBD += qsrv.dbd
endif

# Finally link IOC to the EPICS Base libraries
ISTTOKrpi_LIBS += $(EPICS_BASE_IOC_LIBS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD EXTRA GNUMAKE RULES BELOW HERE

# Explicit dependency needed for generated header file
devISTTOKrpiVersion$(DEP): $(COMMON_DIR)/$(GENVERSION)
