#!/bin/bash
#
#JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
#JAVA_HOME=/opt/java/jdk/jdk1.8.0_231
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
PATH=$JAVA_HOME/bin:$PATH
#cd /home/oper/CSS-Archive/archive-engine-4.1.0
cd /home/oper/CSS-Archive/archive-engine-4.6.6
#/home/esther/EPICS/archive-engine-4.1.0
#./ArchiveEngine -pluginCustomization isttok.ini -engine isttokDB -port 4812&
./archive-engine.sh -engine isttokDB -port 4812 -settings isttok.ini

#sleep 2s
#echo "Archive Started. Check browser at  http://localhost:4812/main"


