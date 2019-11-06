importPackage(Packages.org.csstudio.opibuilder.scriptUtil);
importPackage(Packages.org.csstudio.platform.data);

var cbs = PVUtil.getString(pvArray[0]);
var cbs3 = PVUtil.getString(pvArray[1]);
var logical_slot = PVUtil.getDouble(pvArray[2]);
var addr_type = PVUtil.getDouble(pvArray[3]);
var pv_name = PVUtil.getString(pvArray[4]).replace("\"", "");
var property_name = PVUtil.getString(pvArray[5]).replace("\"", "");

var addr = [6, 9, 7, 8, 5, 10, 4, 11, 3, 12, 2, 13, 1, 14]
var slot;

try{
	slot = addr[logical_slot - 1];
}catch(err){
	slot = 0;
}

if(addr_type == 1){
	slot = logical_slot;
}

var name = cbs + "-" + cbs3 + ":S" + slot + "-"+ pv_name;

if (slot > 0){
	widget.setPropertyValue(property_name,name);
}else{
	widget.setPropertyValue(property_name,"");
}