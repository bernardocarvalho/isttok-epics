importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var cbs = PVUtil.getString(pvArray[0]);
var cbs3 = PVUtil.getString(pvArray[1]);
var slot = PVUtil.getDouble(pvArray[2]);
var pv_name = PVUtil.getString(pvArray[3]).replace("\"", "");

var name = cbs + "-" + cbs3 + ":IO-B" + slot + "-"+ pv_name;
widget.setPropertyValue("pv_name",name);