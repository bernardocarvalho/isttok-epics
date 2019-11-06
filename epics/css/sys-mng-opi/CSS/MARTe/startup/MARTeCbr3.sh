#Start-up script for the MARTe
#!/bin/sh 

if [ -z "$1" ]; then
	echo "Please specify the location of the configuration file"
	exit
else
	echo "Going to start MARTe with the configuration specified in: " $1
fi

target=`uname`
case ${target} in
    Darwin)
    TARGET=macosx
    ;;
    SunOS)
    TARGET=solaris
    ;;
    *)
    TARGET=linux
    ;;
esac

echo "Target is $TARGET"

BASEDIR=/opt/MARTe

CODE_DIRECTORY=$BASEDIR
LD_LIBRARY_PATH=.:$CODE_DIRECTORY/BaseLib2/${TARGET}/

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CODE_DIRECTORY/MARTe/MARTeSupportLib/${TARGET}/

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CODE_DIRECTORY/IOGAMs/${TARGET}/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CODE_DIRECTORY/IOGAMs/LinuxTimer/${TARGET}/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CODE_DIRECTORY/IOGAMs/GenericTimerDriver/${TARGET}/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CODE_DIRECTORY/IOGAMs/StreamingDriver/${TARGET}/

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CODE_DIRECTORY/GAMs/WebStatisticGAM/${TARGET}/

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CODE_DIRECTORY/Interfaces/HTTP/CFGUploader/${TARGET}/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CODE_DIRECTORY/Interfaces/HTTP/SignalHandler/${TARGET}/


LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../IOGAMs/ATCAadc/${TARGET}/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../IOGAMs/FileReader_ATCAadc/${TARGET}/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../GAMs/isttokbiblio/${TARGET}/

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../GAMs/NewAlgorithmGAM/${TARGET}/

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../Interfaces/EPICSLib/${TARGET}/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../Interfaces/EPICSGAM/${TARGET}/

LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../Interfaces/TCPMessageHandler/${TARGET}/
LD_LIBRARY_PATH=$LD_LIBRARY_PATH:../Interfaces/TCPConfigurationHandler/${TARGET}/

if [ ${TARGET} == "macosx" ]; then
    export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:$LD_LIBRARY_PATH
    echo $DYLD_LIBRARY_PATH
else
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
    echo $LD_LIBRARY_PATH
fi

$CODE_DIRECTORY/MARTe/${TARGET}/MARTe_SysM3.ex $1
