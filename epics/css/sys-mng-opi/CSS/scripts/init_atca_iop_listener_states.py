from org.csstudio.opibuilder.scriptUtil import PVUtil, ConsoleUtil, ScriptUtil
from org.eclipse.gef import EditPartListener
from org.csstudio.utility.pv import PVFactory, PVListener
from org.eclipse.jface.dialogs import MessageDialog

cbs = PVUtil.getString(pvArray[1]);
cbs3 = PVUtil.getString(pvArray[2]);
pv_name = PVUtil.getString(pvArray[3]).replace("\"", "");

pvs_test = []

range_init = 0;
range_end = 14;
pv_index_offset = 3;

for i in range (range_init, range_end):
	name = cbs + "-" + cbs3 + ":S" + str(int(i + 1)) + "-" + pv_name
	try:
		pvs_test.append(PVFactory.createPV(name))
	except:
		ConsoleUtil.writeInfo("Exception creating PV: " + name);

class MyPVListener(PVListener):
	def pvValueUpdate(self, pv):
		try:
			pv_name_rec = str(pv);
			pv_name_finish = pv_name_rec[pv_name_rec.index(":S") + len(":S"):]
			board = pv_name_finish[:pv_name_finish.index("-")]		
			pv_index = pv_index_offset + int(board);

			try:
				pvs[pv_index].setValue(PVUtil.getDouble(pv));
			except:
				pass
		except:
			ConsoleUtil.writeInfo("Exception on listener " + str(pv));

for i in range (range_init, range_end):
	try:
		pvs_test[i].start()
	except:
		ConsoleUtil.writeInfo("Cannot start: " + str(i));
	try:
		pvs_test[i].addListener(MyPVListener())
	except:
		ConsoleUtil.writeInfo("Cannot add listener: " + str(i));

class OPICloseListener(EditPartListener):
    def partDeactivated(self, editpart):
	pv_board.stop()
	for i in range (range_init, range_end):
		try:
			pvs_test[i].stop()
			pvs_test[i].removeListener(MyPVListener())
		except:
			ConsoleUtil.writeInfo("Exception removing listener for PV: [" + str(i) + "]");

widget.addEditPartListener(OPICloseListener())
