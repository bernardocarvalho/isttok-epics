from org.csstudio.opibuilder.scriptUtil import PVUtil, ConsoleUtil, ScriptUtil
from org.eclipse.gef import EditPartListener
from org.csstudio.utility.pv import PVFactory, PVListener
from org.eclipse.jface.dialogs import MessageDialog

cbs = PVUtil.getString(pvArray[1]);
cbs3 = PVUtil.getString(pvArray[2]);
pv_name = PVUtil.getString(pvArray[3]).replace("\"", "");

pvs_test = []
pv_board = PVFactory.createPV("loc://atca_iop_sel_slot")
pv_board.start()

for i in range (3, 18):
#	ConsoleUtil.writeWarning("i = " + str(i));
	name = cbs + "-" + cbs3 + ":IO-B" + str(int(i)) + "-" + pv_name
	try:
		pvs_test.append(PVFactory.createPV(name))
	except:
		ConsoleUtil.writeInfo("Exception creating PV: " + name);

class MyPVListener(PVListener):
	def pvValueUpdate(self, pv):
		#MessageDialog.openInformation(None, "Changed", "Changed")
		try:
			board = PVUtil.getDouble(pv_board)
			#ConsoleUtil.writeInfo("pv_board: " + str(pv_board));
			try:
				#ConsoleUtil.writeInfo("board " + str(board));
				if(str(pv).find(str(int(board))) != -1):					
					#ConsoleUtil.writeInfo("find board " + str(board) + " in " + str(pv));
					pvs[4].setValue(PVUtil.getDouble(pv));
				#else:
					#ConsoleUtil.writeInfo("Cannot find board " + str(board) + " " + str(pv));
			except:
				pass
				#ConsoleUtil.writeInfo("Exception on board listener " + str(pv));


#			ConsoleUtil.writeInfo("changed: " + str(pv));
		except:
			ConsoleUtil.writeInfo("Exception on listener " + str(pv));

for i in range (0, 15):
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
	#ConsoleUtil.writeInfo("Removing listener for PVs");
	for i in range (0, 15):
		try:
			pvs_test[i].stop()
			pvs_test[i].removeListener(MyPVListener())
		except:
			ConsoleUtil.writeInfo("Exception removing listener for PV: [" + str(i) + "]");
			#ConsoleUtil.writeInfo("Exception removing listener for PV: [" + str(i) + "] = " + pvs_test[i]);

widget.addEditPartListener(OPICloseListener())
