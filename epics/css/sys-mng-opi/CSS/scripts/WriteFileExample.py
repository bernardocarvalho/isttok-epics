from org.csstudio.opibuilder.scriptUtil import PVUtil
#Basic Setup

filename3 = "/home/pricardofc/CSS-Workspaces/sys-mng-opi"+display.getWidget("filePathWrite").getPropertyValue("text")
myfile = open(filename3, 'w')
myfile.write(display.getWidget("writeLabel").getPropertyValue("text"))
myfile.close()
