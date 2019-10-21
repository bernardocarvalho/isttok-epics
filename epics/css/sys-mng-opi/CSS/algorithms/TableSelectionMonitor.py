from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.swt.widgets.natives.SpreadSheetTable  import ITableSelectionChangedListener
from java.util import Arrays

header_file = PVUtil.getString(pvs[1])
config_file = PVUtil.getString(pvs[2])
code_file = PVUtil.getString(pvs[3])
code_dir = PVUtil.getString(pvs[4])
alg_name = PVUtil.getString(pvs[5])

table = widget.getTable()

class SelectionListener(ITableSelectionChangedListener):
    def selectionChanged(self, selection):
        for row in selection:
        	alg_name = row[0]

        	
        	header_file = alg_name+"GAM.h"
         	config_file = alg_name+"GAM.cfg"
        	code_file = alg_name+"GAM.cpp"
        	code_dir = alg_name+"GAM"
        	    	
        	
        	pvs[1].setValue(header_file)
        	pvs[2].setValue(config_file)
        	pvs[3].setValue(code_file)
        	pvs[4].setValue(code_dir)
        	pvs[5].setValue(alg_name)
        	
        	filename = "/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/gams/"+code_dir+"/"+alg_name+"GAM.for"
        	try:
        		myfile = open(filename, 'r')
        		text = myfile.read()
        		display.getWidget("ExpressTextInputFormula").setPropertyValue("text", text)
        	except:
        		display.getWidget("ExpressTextInputFormula").setPropertyValue("text", "")     		
        	else:
        		myfile.close()
        		
        	filename = "/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/gams/"+code_dir+"/"+alg_name+"GAM.cod"
        	try:
        		myfile = open(filename, 'r')
        		text = myfile.read()
        		display.getWidget("contentCodeLabel2").setPropertyValue("text", text)
        	except:
        		display.getWidget("contentCodeLabel2").setPropertyValue("text", "")     		
        	else:
        		myfile.close()
        	
        	widget.executeAction(0)
                
table.addSelectionChangedListener(SelectionListener())


