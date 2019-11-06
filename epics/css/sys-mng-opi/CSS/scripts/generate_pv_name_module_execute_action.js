importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var cbs = PVUtil.getString(pvArray[0]);
var cbs3 = PVUtil.getString(pvArray[1]);
var slot = PVUtil.getDouble(pvArray[2]);
var state = PVUtil.getDouble(pvArray[3]);
var pv_name = PVUtil.getString(pvArray[4]).replace("\"", "");

var command = "caput " + cbs + "-" + cbs3 + ":IO-B" + slot + "-"+ pv_name + " " + state;
ScriptUtil.executeSystemCommand(command, 1);