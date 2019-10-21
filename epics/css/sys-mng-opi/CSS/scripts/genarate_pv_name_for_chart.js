importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.org.csstudio.utility.pv);

var cbs = PVUtil.getString(pvArray[0]);
var cbs3 = PVUtil.getString(pvArray[1]);
var slot = PVUtil.getDouble(pvArray[2]);
var channel = "" + PVUtil.getDouble(pvArray[3]);
var dec = PVUtil.getDouble(pvArray[4]);
var pv_name = PVUtil.getString(pvArray[5]).replace("\"", "");

if (channel < 10){
	channel = "0" + channel;
}

var name = cbs + "-" + cbs3 + ":IO-B" + slot + "C" + channel + "-"+ pv_name;

var val = (dec/200)*1000;
var val_str = "Time (x" + val + " us)"

widget.setPropertyValue("trace_0_y_pv",name);
widget.setPropertyValue("axis_0_axis_title",val_str);
