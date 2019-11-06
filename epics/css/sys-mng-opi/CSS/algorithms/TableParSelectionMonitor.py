from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.swt.widgets.natives.SpreadSheetTable  import ITableSelectionChangedListener
from java.util import Arrays

table = widget.getTable()

class SelectionListener(ITableSelectionChangedListener):
    def selectionChanged(self, selection):
        for row in selection:
        	par_name = row[1]
        	par_io = row[4]
        	pvs[1].setValue(par_name)
        	pvs[2].setValue(par_io)
        	      	
table.addSelectionChangedListener(SelectionListener())


