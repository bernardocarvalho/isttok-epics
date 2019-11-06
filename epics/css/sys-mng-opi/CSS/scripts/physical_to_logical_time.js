importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.org.csstudio.platform.data);

var cbs = PVUtil.getString(pvArray[0]);
var cbs3 = PVUtil.getString(pvArray[1]);
var physical_slot = PVUtil.getDouble(pvArray[2]);
var addr_type = PVUtil.getDouble(pvArray[3]);
var pv_name = PVUtil.getString(pvArray[4]).replace("\"", "");
var property_name = PVUtil.getString(pvArray[5]).replace("\"", "");

var addr = [13, 11, 9, 7, 5, 1, 3, 4, 2, 6, 8, 10, 12, 14]
var slot;
var board_type = "TS";

ConsoleUtil.writeInfo("addr_type: " + addr_type);

// 0 - Physical
// 1 - Logical

if(addr_type == 1){
	try{
		slot = addr[physical_slot - 1];
	}catch(err){
		slot = 0;
	}
}else{
	slot = physical_slot;
}

if (slot == 1 || slot == 2){
	board_type = "TS";
}else{
	board_type = "IO";
}	

ConsoleUtil.writeInfo("slot: " + slot);

var name = cbs + "-" + cbs3 + ":" + board_type + "-" + "B" + slot + "-" + pv_name;

if (slot > 0){
	widget.setPropertyValue(property_name, name);
}else{
	widget.setPropertyValue(property_name, "");
}