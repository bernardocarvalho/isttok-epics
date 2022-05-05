#!/bin/bash
#
JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
#PATH=$JAVA_HOME/bin:$PATH
#cd /home/oper/CSS-Archive/archive-engine-4.1.0
TOP="/home/oper/CSS-Archive/archive-engine-4.6.6"
# CSS_ARCH_HOME=/home/oper/CSS-Archive/archive-engine-4.6.6
cd $TOP
#./ArchiveEngine -pluginCustomization isttok.ini -engine isttokDB -port 4812&
#./archive-engine.sh -engine isttokDB -port 4812 -settings isttok.ini
#JAR=`echo "${TOP}/service-archive-engine-*.jar"`
JAR=$(ls service-archive-engine-*.jar)
#$JAVA_HOME/bin/java -jar $JAR $OPT "$@"
$JAVA_HOME/bin/java -jar $JAR  -engine isttokDB -port 4812 -settings isttok.ini -noshell

#sleep 2s
#echo "Archive Started. Check browser at  http://localhost:4812/main"


