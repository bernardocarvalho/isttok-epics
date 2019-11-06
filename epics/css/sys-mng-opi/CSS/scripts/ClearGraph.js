importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.org.eclipse.jface.dialogs);

//var pvLastPulseNumber = PVUtil.getDouble(pvArray[0]);
//var pvCurrPulseNumber = PVUtil.getDouble(pvArray[1]);
//widgetController.clearGraph();

var name = PVUtil.getString(pvArray[1]).replace("\"", "");

display.getWidget(name).clearGraph();
