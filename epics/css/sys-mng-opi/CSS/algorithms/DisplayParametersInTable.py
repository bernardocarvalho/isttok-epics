from org.csstudio.opibuilder.scriptUtil import PVUtil
from org.csstudio.opibuilder.scriptUtil import ColorFontUtil

alg_name2 = PVUtil.getString(pvs[0])

table = widget.getTable()
i = 0
j = 0
row = 0
col = 0
mylist = []
filename = "/home/opertok/CSS-Workspaces/sys-mng-opi/CSS/algorithms/"+alg_name2+".par"

try:
	file = open(filename, 'r')
	
	for i in range(table.getRowCount()):
		for j in range(table.getColumnCount()):
			table.setCellText(i, j, "")
	
	i = 0
	j = 0
	
	for line in file:
		mylist.insert(i, line)
		table.setCellText(row, col, mylist[i].strip('\n'))
		i = i+1
		col = col+1
		if i == ( 8*(row+1) ):
			row = row+1
   			col = 0
except:
	a = 0
else:
	file.close()