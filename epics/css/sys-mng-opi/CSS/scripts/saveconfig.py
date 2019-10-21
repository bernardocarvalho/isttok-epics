from org.csstudio.opibuilder.scriptUtil import PVUtil
from decimal import Decimal

val = PVUtil.getDouble(pvs[0])
if  val == 1:
	val = 0
	pvs[0].setValue(val)
	
	filename = "/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/gams"+display.getWidget("FileNameTextInput").getPropertyValue("text")+".cfg"

	myfile = open(filename, 'w')
	myfile.write('+')
	myfile.write(display.getWidget("FileNameTextInput").getPropertyValue("text"))
	myfile.write(' = {\n')
	myfile.write(display.getWidget("contentInputLabel").getPropertyValue("text"))
	myfile.write('\n')
	myfile.write(display.getWidget("contentOutputLabel").getPropertyValue("text"))
	myfile.write('\n')
	myfile.write('}\n')
	myfile.close()