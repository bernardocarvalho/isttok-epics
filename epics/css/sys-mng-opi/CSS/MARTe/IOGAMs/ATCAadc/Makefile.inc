#*******************************************************************************
#      $Log: Makefile.inc,v $
#      Revision 1.8  2009/03/11 12:31:54  aneto
#      Support an html output with information about the driver
#
#      Revision 1.7  2009/03/06 10:01:17  ppcc_dev
#      Added automatic compilation
#
#      Revision 1.6  2008/09/08 09:18:01  ppcc_dev
#      Added a break in the switch sentence of TimeInputGAM.
#      Removed the pcieATCA module from standard compilation scripts
#
#      Revision 1.5  2008/09/05 11:08:35  ppcc_dev
#      Added module compilation
#
#      Revision 1.4  2008/08/20 16:34:36  ppcc_dev
#      Added PulseStart to reset the internal counter to 0 when using the SoftTrigger option
#
#      Revision 1.3  2008/08/01 14:09:56  rvitelli
#      *** empty log message ***
#
#      Revision 1.2  2008/06/16 14:39:23  rvitelli
#      *** empty log message ***
#
#      Revision 1.1  2008/06/05 13:18:58  rvitelli
#      Skeleton of Drv files and makefiles
#
#
#*******************************************************************************/

OBJSX=
SPB=

CODEDIR=/opt/MARTe
DRIVERDIR=/opt/drivers/ATCA-MIMO
MAKEDEFAULTDIR=$(CODEDIR)/MakeDefaults


include $(MAKEDEFAULTDIR)/MakeStdLibDefs.$(TARGET)

CFLAGS+= -I.
CFLAGS+= -I$(CODEDIR)/GAMs/WebStatisticGAM
CFLAGS+= -I$(CODEDIR)/MARTe/MARTeSupportLib
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level0
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level1
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level2
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level3
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level4
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level5
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level6
CFLAGS+= -I$(CODEDIR)/BaseLib2/LoggerService
CFLAGS+= -I$(DRIVERDIR)/include

all:	$(OBJS) $(SUBPROJ) $(TARGET)/ATCAadcDrv$(GAMEXT) \
	                   $(TARGET)/driver_test$(EXEEXT)
	echo  $(OBJS)

include depends.$(TARGET)

include $(MAKEDEFAULTDIR)/MakeStdLibRules.$(TARGET)


