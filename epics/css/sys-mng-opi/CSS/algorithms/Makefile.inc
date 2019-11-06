OBJSX=

#########################################################
# MANDATORY: POINT THIS TO YOUR MARTE CODE DIRECTORY!!! #
#########################################################
CODEDIR=/opt/MARTe


MAKEDEFAULTDIR=$(CODEDIR)/MakeDefaults
include $(MAKEDEFAULTDIR)/MakeStdLibDefs.$(TARGET)

CFLAGS+= -I.
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level0
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level1
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level2
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level3
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level4
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level5
CFLAGS+= -I$(CODEDIR)/BaseLib2/Level6
CFLAGS+= -I$(CODEDIR)/BaseLib2/LoggerService

all:	$(OBJS)\
        $(TARGET)/NewAlgorithmGAM$(GAMEXT)
	    echo  $(OBJS)

include depends.$(TARGET)

include $(MAKEDEFAULTDIR)/MakeStdLibRules.$(TARGET)


