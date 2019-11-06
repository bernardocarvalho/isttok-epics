importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var cbs = PVUtil.getString(pvArray[0]);
var cbs3 = PVUtil.getString(pvArray[1]);
var slot = PVUtil.getDouble(pvArray[2]);
var channel = "" + PVUtil.getDouble(pvArray[3]);
var pv_name = PVUtil.getString(pvArray[4]).replace("\"", "");

if (channel < 10){
	channel = "0" + channel;
}

var name = cbs + "-" + cbs3 + ":IO-B" + slot + "C" + channel + "-"+ pv_name;
widget.setPropertyValue("pv_name",name);