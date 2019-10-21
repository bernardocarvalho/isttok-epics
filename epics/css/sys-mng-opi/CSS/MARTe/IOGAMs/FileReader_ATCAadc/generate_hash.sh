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
# $Id$
#
#############################################################
#Start-up script for the MARTe
#!/bin/sh 

args=("$@")
nargs=$#

user=${args[0]}
pass=${args[1]}
realm=${args[2]}

if [ $nargs -eq 3 ];then

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

	LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./${TARGET}/

	if [ ${TARGET} == "macosx" ]; then
		export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:$LD_LIBRARY_PATH
		echo $DYLD_LIBRARY_PATH
	else
		export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
		echo $LD_LIBRARY_PATH
	fi

	./${TARGET}/generate_hash.ex $user $pass $realm

else
	echo "Invalid number of arguments [$nargs]. Usage: generate_hash.sh <username> <password> <realm>"
fi
