importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.java.io);

var filePath = display.getWidget("filePathWrite").getPropertyValue("text");
var text = display.getWidget("textInput").getPropertyValue("text");
FileUtil.writeTextFile(filePath, true, text, false);
