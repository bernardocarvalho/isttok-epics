from org.csstudio.opibuilder.scriptUtil import PVUtil, ConsoleUtil, ScriptUtil
from org.eclipse.gef import EditPartListener
from org.csstudio.utility.pv import PVFactory

pv_cbs = PVFactory.createPV("loc://atca_iop_cbs")
pv_cbs_3 = PVFactory.createPV("loc://atca_iop_cbs3")
pv_cbs_3_rt = PVFactory.createPV("loc://atca_iop_rt_cbs3")
pv_cbs_3_sm = PVFactory.createPV("loc://atca_iop_sm_cbs3")
pv_sel_slot = PVFactory.createPV("loc://atca_iop_sel_slot")
pv_fir_fixed = PVFactory.createPV("loc://atca_iop_fir_fixed")
pv_board_order = PVFactory.createPV("loc://atca_iop_order")

val_cbs = "0.000"
val_cbs3 = "0.000"
val_cbs3_rt = "0.000"
val_cbs3_sm = "0.000"
val_sel_slot = 0
val_fir_fixed = 0
val_order = "0.000"

try:
	pv_cbs.start();
	val_cbs = PVUtil.getString(pv_cbs)

	if val_cbs == "0.000":
		pv_cbs.setValue("TEST-PTYP");
except:
	pass


try:
	pv_cbs_3.start();
	val_cbs3 = PVUtil.getString(pv_cbs_3)

	if val_cbs3 == "0.000":
		pv_cbs_3.setValue("ATCA");
except:
	pass

try:
	pv_cbs_3_rt.start();
	val_cbs3_rt = PVUtil.getString(pv_cbs_3_rt)

	if val_cbs3_rt == "0.000":
		pv_cbs_3_rt.setValue("MT01");
except:
	pass

try:
	pv_cbs_3_sm.start();
	val_cbs3_sm = PVUtil.getString(pv_cbs_3_sm)

	if val_cbs3_sm == "0.000":
		pv_cbs_3_sm.setValue("SM01");
except:
	pass

try:
	pv_sel_slot.start();
	val_sel_slot = PVUtil.getDouble(pv_sel_slot)

	if val_sel_slot == 0:
		pv_sel_slot.setValue(13);
except:
	pass

try:
	pv_fir_fixed.start();
	val_fir_fixed = PVUtil.getDouble(pv_fir_fixed)

	if val_fir_fixed == 0:
		pv_fir_fixed.setValue(10);
except:
	pass

try:
	pv_board_order.start();
	val_order = PVUtil.getString(pv_board_order)

	if val_order == "0.000":
		pv_board_order.setValue("Physical");
except:
	pass

val_acq_type = "0.000"
val_adc_scale = 0

pv_acq_type = PVFactory.createPV("loc://atca_iop_fir_type")
pv_adc_scale = PVFactory.createPV("loc://atca_iop_dr_use_scale")

try:
	pv_acq_type.start();
	val_acq_type = PVUtil.getString(pv_acq_type)

	if val_acq_type == "0.000":
		pv_acq_type.setValue("CA");
except:
	pass


try:
	pv_adc_scale.start();
	val_adc_scale = PVUtil.getDouble(pv_adc_scale)

	if val_sel_slot == 0:
		val_adc_scale.setValue(1);
except:
	pass

pv_channel = []
pv_update = []
pv_amp = []
pv_signal = []

for i in range (0, 48):
	ch_number = ""
	if i < 10:
		ch_number = "0" + str(i)
	else:
		ch_number = str(i)
#	ConsoleUtil.writeWarning("i = " + str(i));
	pv_channel.append(PVFactory.createPV("loc://atca_iop_channel" + ch_number))
	pv_update.append(PVFactory.createPV("loc://update" + ch_number))
	pv_amp.append(PVFactory.createPV("loc://amp" + ch_number))
	pv_signal.append(PVFactory.createPV("loc://wf" + ch_number))

for i in range (0, 48):

	val_channel = 0
	val_update = 0
	val_amp = 0
	val_signal = "0.000"

	try:
		pv_channel[i].start()
		val_channel = PVUtil.getDouble(pv_channel[i])

		if val_channel == 0:
			pv_channel[i].setValue(i)
	except:
		pass

	try:
		pv_update[i].start()
		val_update = PVUtil.getDouble(pv_update[i])

		if val_update == 0:
			pv_update[i].setValue(100)
	except:
		pass

	try:
		pv_amp[i].start()
		val_amp = PVUtil.getDouble(pv_amp[i])

		if val_amp == 0:
			pv_amp[i].setValue(10)
	except:
		pass


	try:
		pv_signal[i].start()
		val_signal = PVUtil.getString(pv_signal[i])

		if val_signal == "0.000":
			pv_signal[i].setValue("sin")	
	except:
		pass

class OPICloseListener(EditPartListener):
    def partDeactivated(self, editpart):

	ScriptUtil.executeSystemCommand("pkill -9 testAO-wave", 1);  

	pv_cbs.stop();
	pv_cbs_3.stop();
	pv_cbs_3_rt.stop();
	pv_cbs_3_sm.stop();
	pv_sel_slot.stop();
	pv_fir_fixed.stop();
	pv_acq_type.stop();
	pv_adc_scale.stop();
	pv_board_order.stop();

	for i in range (0, 8):
		pv_channel[i].stop()
		pv_update[i].stop()
		pv_amp[i].stop()	
		pv_signal[i].stop()

widget.addEditPartListener(OPICloseListener())
