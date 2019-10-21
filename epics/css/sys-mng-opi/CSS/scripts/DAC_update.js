importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.org.eclipse.jface.dialogs);
importPackage(Packages.org.csstudio.platform.data);
importPackage(Packages.java.lang);

var state = PVUtil.getDouble(pvArray[0]);
var channel_id = PVUtil.getDouble(pvArray[1]);
var board_slot = PVUtil.getDouble(pvArray[2]);
var wf = PVUtil.getString(pvArray[3]);
var amp = PVUtil.getDouble(pvArray[4]);
var update = PVUtil.getDouble(pvArray[5]);

var amp_calc = parseInt( (amp*131071)/10 );

ConsoleUtil.writeInfo("DAC_update");

if (channel_id < 10){
	channel_id = "0" + channel_id;
}

// var command = "/opt/codac/examples/atca-io-processor-api/testAO-wave "+board_slot+" "+channel_id+" "+update+" "+wf+" "+amp_calc+" 100";
//var command = "/home/codac-dev/m-kmod-atca-io-processor/branches/test-hr/src/main/c/examples/testAO-wave "+board_slot+" "+channel_id+" "+update+" "+wf+" "+amp_calc+" 100";
var command = "/home/codac-dev/Documents/m-epics-xtca-iop/atca-io-processor/c/examples/testAO-wave "+board_slot+" "+channel_id+" "+update+" "+wf+" "+amp_calc+" 100";
if (state == 1){
	if (update > 0){
		display.getWidget("wf" + channel_id + "ComboBox").setPropertyValue("enabled", false);
	    	display.getWidget("amp" + channel_id + "TextInput").setPropertyValue("enabled", false);
		display.getWidget("update" + channel_id + "TextInput").setPropertyValue("enabled", false);
	    	ScriptUtil.executeSystemCommand(command, 1);
	}else{
		MessageDialog.openError(null, "Error", "Invalid update rate. Must be positive!");
		pvs[0].setValue(0);
	}
}else{
	ScriptUtil.executeSystemCommand("pkill -9 testAO-wave", 1);  
	display.getWidget("wf" + channel_id + "ComboBox").setPropertyValue("enabled", true);
    	display.getWidget("amp" + channel_id + "TextInput").setPropertyValue("enabled", true);
	display.getWidget("update" + channel_id + "TextInput").setPropertyValue("enabled", true);
}
