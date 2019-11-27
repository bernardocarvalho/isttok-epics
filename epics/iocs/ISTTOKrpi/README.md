### ISTTOK Epics IOC running in the Raspberry Pi Central Control 

## Steps 
1. Install epics on Rpi Linux. You need to install the following required support modules 
	1. [ASYN](https://github.com/epics-modules/asyn.git)
	2. [StreamDevice](https://github.com/paulscherrerinstitute/StreamDevice.git)
	3. [Sequencer](https://www-csr.bessy.de/control/SoftDist/sequencer/Installation.html)
	4. I2C driver, [drvAsynI2C](https://github.com/ffeldbauer/drvAsynI2C)

2. Goto $HOME folder and Run
	* `git clone  https://bernardo@git.ipfn.tecnico.ulisboa.pt/r/ISTTOK.git
	* `cd ISTTOK`
	* `epics/iocs/ISTTOKrpi`
	* `make`
	
## Start the IOC on power up
	1. Make sure `screen` is installed in Linux
	2. Include following Line in /etc/rc.local
     		* `screen -dm bash -c "cd [..]/ISTTOKrpi/iocBoot/iocISTTOKrpi; ../../bin/linux-arm/ISTTOKrpi st.cmd"`
	3. To access EPICS console run
     		* `sudo screen -r`

