from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil


table = widget.getTable()

#Fill PV Name only once
if widget.getVar("firstTime") == None:
    widget.setVar("firstTime", True)
    i=0
    for pv in pvs:
        table.setCellText(i, 0, pv.getName())
        if not pv.isConnected():
            table.setCellText(i, 1, "Disconnected")
        i+=1

#find index of the trigger PV
i=0
while triggerPV != pvs[i]:
    i+=1

table.setCellText(i, 1, PVUtil.getString(triggerPV))
table.setCellText(i, 2, PVUtil.getTimeString(triggerPV))