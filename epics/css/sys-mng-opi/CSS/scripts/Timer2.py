from org.csstudio.opibuilder.scriptUtil import PVUtil, ConsoleUtil, ColorFontUtil
from java.lang import Thread, Runnable

startButton2 = display.getWidget("Start_Button2")
stopButton2 = display.getWidget("Stop_Button2")
resetButton2 = display.getWidget("Reset_Button2")

bar2 = display.getWidget("Progress_Bar2")
startb2 = display.getWidget("Start_Boolean_Button_1")

hourText2 = display.getWidget("hourText2")
hourPV2=hourText2.getPV()
minText2 = display.getWidget("minText2")
minPV2=minText2.getPV()
secText2 = display.getWidget("secText2")
secPV2=secText2.getPV()

timerLabel2 = display.getWidget("timerLabel2")


class Timer2(Runnable):
    def run(self):
        startButton2.setEnabled(True)
        stopButton2.setEnabled(True)
        resetButton2.setEnabled(True)

        hourText2.setEnabled(True)
        minText2.setEnabled(True)
        secText2.setEnabled(True)   
        hour2 = 0
        min2 = 30
        sec2 = 0
        timerLabel2.setPropertyValue("foreground_color", ColorFontUtil.BLACK)
        timerLabel2.setPropertyValue("text", "Timer")
        stopped=False
        total2 = hour2*3600+min2*60+sec2
        for i in range(total2,-1,-1):
            if not display.isActive():
                return
            if PVUtil.getLong(pvs[0])==0:
                stopped = True
                break
            pvs[1].setValue(100-100*i/total2)
            hourPV2.setValue(int(i/3600))
            minPV2.setValue(int(i%3600/60))
            secPV2.setValue(int(i%60))
            Thread.sleep(1000)
            
        timerLabel2.setPropertyValue("foreground_color", ColorFontUtil.BLACK)
        if stopped:
            bar2.getPV().setValue(0)
            timerLabel2.setPropertyValue("text", "Stopped!")
            if PVUtil.getDouble(pvs[3]) == 1:
                pvs[0].setValue(1)
            else:
                pvs[0].setValue(0)
            hourPV2.setValue(hour2)
            minPV2.setValue(min2)
            secPV2.setValue(sec2)           
        else:
            bar2.getPV().setValue(0)
            pvs[0].setValue(0)
            timerLabel2.setPropertyValue("text", "Timeout!")
            widget.executeAction(0)
            hourPV2.setValue(hour2)
            minPV2.setValue(min2)
            secPV2.setValue(sec2)  
            pvs[2].setValue(0)

        startButton2.setEnabled(True)
        stopButton2.setEnabled(True)
        resetButton2.setEnabled(True)

        hourText2.setEnabled(True)
        minText2.setEnabled(True)
        secText2.setEnabled(True)

if PVUtil.getLong(pvs[0])==1:
	thread =Thread(Timer2());
	thread.start()
