target=linux
BASEDIR=/opt/MARTe

OBJS =
OBJS += $(target)/AdvancedConfigurator.o
OBJS += $(target)/ControllerGAM.o
OBJS += $(target)/CosineProbeGAM.o
OBJS += $(target)/ElectricProbesGAM.o
OBJS += $(target)/ElectrodeBiasingGAM.o
OBJS += $(target)/FireSignalDischargeStatusGAM.o
OBJS += $(target)/HAlphaGAM.o
OBJS += $(target)/HeavyIonBeamGAM.o
OBJS += $(target)/IntegerSequentialControl.o
OBJS += $(target)/InterferometryGAM.o
OBJS += $(target)/IPID.o
OBJS += $(target)/IWaveform.o
OBJS += $(target)/MachineProtectionGAM.o
OBJS += $(target)/MagneticsGAM.o
OBJS += $(target)/MainConfigurator.o
OBJS += $(target)/MainRogowskiGAM.o
OBJS += $(target)/PlasmaStatusGAM.o
OBJS += $(target)/PowerSupplyCommunicatorGAM.o
OBJS += $(target)/SineProbeGAM.o
OBJS += $(target)/SpectroscopyTriggerGAM.o
OBJS += $(target)/SVGGraphicSupport.o
OBJS += $(target)/TechnicalSignalsGAM.o
OBJS += $(target)/TimeWindowsGAM.o
OBJS += $(target)/TomographyGAM.o
OBJS += $(target)/UFSerialUART.o
OBJS += $(target)/WaveformGAM.o 

#CFLAGS = -m32
CFLAGS = -fPIC
CFLAGS += -I.
CFLAGS += -I$(BASEDIR)/BaseLib2/Level0
CFLAGS += -I$(BASEDIR)/BaseLib2/Level1
CFLAGS += -I$(BASEDIR)/BaseLib2/Level2
CFLAGS += -I$(BASEDIR)/BaseLib2/Level3
CFLAGS += -I$(BASEDIR)/BaseLib2/Level4
CFLAGS += -I$(BASEDIR)/BaseLib2/Level5
CFLAGS += -I$(BASEDIR)/BaseLib2/Level6

LIBRARY_PATH += -L$(BASEDIR)/BaseLib2/linux
LIBRARIES = -lBaseLib2

CFLAGSPEC= -D_LINUX -DUSE_PTHREAD -pthread

all : $(OBJS)
	gcc -O3 $(CFLAGS) $(LIBRARY_PATH) -shared -fPIC $(OBJS) $(LIBRARIES) -o $(target)/isttokbiblio.so
	touch $(target)/libisttokbiblio.so
	rm $(target)/libisttokbiblio.so
	ln -fns isttokbiblio.so $(target)/libisttokbiblio.so

linux/%.o : %.cpp
	gcc -O3 -c $(CFLAGS) $(CFLAGSPEC) $(LIBRARY_PATH) $(LIBRARIES) $*.cpp -o $(target)/$*.o

clean:
	rm -f $(target)/depends*
	rm -f $(target)/*.o
	rm -f $(target)/*.a
	rm -f $(target)/*.so
	rm -f $(target)/*.ex
