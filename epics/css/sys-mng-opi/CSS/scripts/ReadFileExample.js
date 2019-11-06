importPackage(Packages.org.csstudio.opibuilder.scriptUtil);

var filePath = display.getWidget("filePathRead").getPropertyValue("text");
var text = FileUtil.readTextFile(filePath);
display.getWidget("readLabel").setPropertyValue("text", text);
