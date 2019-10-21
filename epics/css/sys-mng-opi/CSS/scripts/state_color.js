importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.org.eclipse.jface.dialogs);
importPackage(Packages.java.lang);

var state_default = PVUtil.getDouble(pvArray[0]);
var state_log_phy = PVUtil.getDouble(pvArray[1]);
var state_phy_log = PVUtil.getDouble(pvArray[2]);
var addr_type = PVUtil.getDouble(pvArray[3]);
var order = PVUtil.getString(pvArray[4]);

var val = state_default;

if(addr_type == 1){
	if (order == "Physical"){
		val = state_log_phy;
	}
}else{
	if (order == "Logical"){
		val = state_phy_log;
	}
}

switch(val){
	case 0:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(255,255,255) );
		break;
	case 1:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(229,229,229) );
		break;
	case 2:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(205,216,192) );
		break;
	case 3:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(145,180,145) );
		break;
	case 4:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(120,245,120) );
		break;
	case 5:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(255,255,100) );
		break;
	case 6:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(255,165,0) );
		break;
	case 7:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(255,80,0) );
		break;
	case 8:
		widget.setPropertyValue("background_color", ColorFontUtil.getColorFromRGB(200,100,200) );
		break;
}