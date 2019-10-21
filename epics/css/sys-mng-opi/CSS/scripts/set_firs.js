importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.org.csstudio.opibuilder.util);
importPackage(Packages.java.lang);

var board_slot = PVUtil.getDouble(pvs[0]);
var rate = PVUtil.getDouble(pvs[1]);
var type = PVUtil.getString(pvs[2]);

var path = ResourceUtil.getPathFromString("./");
path = ResourceUtil.buildAbsolutePath(widget.getWidgetModel(), path);
var folderpath= FileUtil.workspacePathToSysPath(path.toString());
var command = "sh " + folderpath + "/scripts/FIR_coef_decim.js "+board_slot +" "+type+" "+rate;
// ConsoleUtil.writeInfo(command);
ScriptUtil.executeSystemCommand(command, 1);

