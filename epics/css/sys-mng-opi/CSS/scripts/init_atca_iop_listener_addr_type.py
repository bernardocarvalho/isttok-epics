from org.csstudio.opibuilder.scriptUtil import PVUtil, ConsoleUtil, ScriptUtil
from org.eclipse.gef import EditPartListener
from org.csstudio.utility.pv import PVFactory, PVListener
from org.eclipse.jface.dialogs import MessageDialog

cbs = PVUtil.getString(pvArray[1]);
cbs3 = PVUtil.getString(pvArray[2]);
pv_name = PVUtil.getString(pvArray[3]).replace("\"", "");
name = cbs + "-" + cbs3 + ":" + pv_name

try:
	pv_epics = PVFactory.createPV(name)
	pv_epics.start()
	pv_epics.setValue(1)
except:
	pass


class MyPVListener(PVListener):
	def pvValueUpdate(self, pv):
		try:
			pvs[4].setValue(PVUtil.getDouble(pv));
		except:
			pass

try:
	pv_epics.addListener(MyPVListener())
except:
	pass
	
class OPICloseListener(EditPartListener):
    def partDeactivated(self, editpart):
	pv_epics.stop()

widget.addEditPartListener(OPICloseListener())
