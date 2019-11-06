from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ScriptUtil
val = PVUtil.getDouble(pvs[0])
if val == 1:
	val = 0
	pvs[0].setValue(val)
	command_remove="rm -rf /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/gams/"+display.getWidget("FileNameTextInput2").getPropertyValue("text")+"GAM"
	ScriptUtil.executeSystemCommand(command_remove,1)
	command_create = "mkdir /home/opertok/CSS-Workspaces/sys-mng-opi/CSS/gams/"+display.getWidget("FileNameTextInput2").getPropertyValue("text")+"GAM"
	ScriptUtil.executeSystemCommand(command_create,1)
	filename = "/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/algorithms/"+display.getWidget("FileNameTextInput2").getPropertyValue("text")+".par"
	text = display.getWidget("contentParameterLabel2").getPropertyValue("text")
	myfile = open(filename, 'w')
	myfile.write(text)
	myfile.close()
	
	filename = "/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/algorithms/"+display.getWidget("FileNameTextInput2").getPropertyValue("text")+".sig"
	text1 = display.getWidget("contentInputLabel2").getPropertyValue("text")
	myfile = open(filename, 'w')
	myfile.write('\tinput_signals = {\n')
	myfile.write(text1)
	myfile.write('\t}\n\n')
	text2 = display.getWidget("contentOutputLabel2").getPropertyValue("text")
	myfile.write('\toutput_signals = {\n')
	myfile.write(text2)
	myfile.write('\t}\n')
	myfile.close()
	
	filename = "/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/algorithms/"+display.getWidget("FileNameTextInput2").getPropertyValue("text")+".xml"
	text = display.getWidget("contentXmlLabel2").getPropertyValue("text")
	myfile = open(filename, 'w')
	myfile.write('<?xml version="1.0"?>\n')
	myfile.write('<macros>\n')
	myfile.write(text)
	myfile.write('</macros>\n')
	myfile.close()
	
	filename = "/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/algorithms/ControlAlgorithms.txt"
	myfile = open(filename, 'r')
	text = myfile.read()
	myfile.close()
	myfile = open(filename, 'w')
	text += display.getWidget("FileNameTextInput2").getPropertyValue("text")+"\n"
	myfile.write(text)
	myfile.close()
	
	pvs[1].setValue(1)