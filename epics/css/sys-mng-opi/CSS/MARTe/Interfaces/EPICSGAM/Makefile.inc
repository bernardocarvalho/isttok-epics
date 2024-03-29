#############################################################
#
# Copyright 2011 EFDA | European Fusion Development Agreement
#
# Licensed under the EUPL, Version 1.1 or - as soon they 
# will be approved by the European Commission - subsequent  
# versions of the EUPL (the "Licence"); 
# You may not use this work except in compliance with the 
# Licence. 
# You may obtain a copy of the Licence at: 
#  
# http://ec.europa.eu/idabc/eupl
#
# Unless required by applicable law or agreed to in 
# writing, software distributed under the Licence is 
# distributed on an "AS IS" basis, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
# express or implied. 
# See the Licence for the specific language governing 
# permissions and limitations under the Licence. 
#
# $Id: Makefile.inc 3 2012-01-15 16:26:07Z aneto $
#
#############################################################
EPICS_PATH=$(EPICS_BASE)
MARTEBasePath=/opt/MARTe

MAKEDEFAULTDIR=$(MARTEBasePath)/MakeDefaults

include $(MAKEDEFAULTDIR)/MakeStdLibDefs.$(TARGET)

OBJSX=  EPICSSignalsTable.x

CFLAGS+= -I.
CFLAGS+= -I$(MARTEBasePath)/
CFLAGS+= -I$(MARTEBasePath)/MARTe/MARTeSupportLib
CFLAGS+= -I$(MARTEBasePath)/BaseLib2/Level0
CFLAGS+= -I$(MARTEBasePath)/BaseLib2/Level1
CFLAGS+= -I$(MARTEBasePath)/BaseLib2/Level2
CFLAGS+= -I$(MARTEBasePath)/BaseLib2/Level3
CFLAGS+= -I$(MARTEBasePath)/BaseLib2/Level4
CFLAGS+= -I$(MARTEBasePath)/BaseLib2/Level5
CFLAGS+= -I$(MARTEBasePath)/BaseLib2/Level6

CFLAGS+= -I$(EPICS_PATH)/include
CFLAGS+= -I$(EPICS_PATH)/include/os/Linux
CFLAGS+= -I$(EPICS_PATH)/include/compiler/gcc
CFLAGS+= -I../EPICSLib

all: $(OBJS) \
	$(TARGET)/EPICSGAM$(GAMEXT)
	echo  $(OBJS)

include depends.$(TARGET)

include $(MAKEDEFAULTDIR)/MakeStdLibRules.$(TARGET)
