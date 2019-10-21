importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.org.csstudio.platform.data);

var cbs = PVUtil.getString(pvArray[0]);
var cbs3 = PVUtil.getString(pvArray[1]);
var slot = PVUtil.getDouble(pvArray[2]);
var addr_type = PVUtil.getDouble(pvArray[3]);
var pv_name = PVUtil.getString(pvArray[4]).replace("\"", "");
var property_name = PVUtil.getString(pvArray[5]).replace("\"", "");
var order = PVUtil.getString(pvArray[6]);

var physical_from_logical = [6, 9, 7, 8, 5, 10, 4, 11, 3, 12, 2, 13, 1, 14]
var logical_from_physical = [13, 11, 9, 7, 5, 1, 3, 4, 2, 6, 8, 10, 12, 14]

var slot_number = slot;

if(addr_type == 1){
	if (order == "Physical"){
		slot_number = logical_from_physical[slot -1];
	}
}else{
	if (order == "Logical"){
		slot_number = physical_from_logical[slot -1];
	}
}

var name = cbs + "-" + cbs3 + ":S" + slot_number + "-"+ pv_name;

if (slot > 0){
	widget.setPropertyValue(property_name,name);
}else{
	widget.setPropertyValue(property_name,"");
}