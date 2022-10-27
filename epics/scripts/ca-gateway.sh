#!/bin/sh
#
# EPICS CA-Gateway deamos launcher
# https://epics.anl.gov/EpicsDocumentation/ExtensionsManuals/Gateway/Gateway.html
#
export EPICS_ROOT=/home/isttok/EPICS
export EPICS_BASE=${EPICS_ROOT}/epics-base
EPICS_HOST_ARCH=`${EPICS_BASE}/startup/EpicsHostArch`
# -cip
# export EPICS_CA_ADDR_LIST="localhost 192.168.0.60 192.168.0.21 192.168.0.22 192.168.0.99"
export EPICS_CA_ADDR_LIST="192.168.1.110 192.168.1.120 192.168.1.152"
export EPICS_CA_AUTO_ADDR_LIST="NO"
# -sip
export EPICS_CAS_INTF_ADDR="193.136.136.88"
# MODULES=${EPICS_ROOT}/modules
EXTENSIONS=${EPICS_ROOT}/extensions
CA_GTW_BASE_BIN=${EXTENSIONS}/ca-gateway/bin/${EPICS_HOST_ARCH}
# -server
${CA_GTW_BASE_BIN}/gateway -log /tmp/ca-gateway.log -archive -no_cache -server
