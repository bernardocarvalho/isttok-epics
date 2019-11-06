importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var cbs = PVUtil.getString(pvArray[0]);
var cbs3 = PVUtil.getString(pvArray[1]);
var addr = PVUtil.getString(pvArray[2]).replace("\"", "");
var pv_name = PVUtil.getString(pvArray[3]).replace("\"", "");

var name = cbs + "-" + cbs3 + ":" + addr + "-"+ pv_name;
widget.setPropertyValue("pv_name",name);