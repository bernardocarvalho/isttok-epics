from org.csstudio.opibuilder.scriptUtil import PVUtil
#General Setup

val0 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomographyR").getPV() ) ))
val1 = display.getWidget("TextInputTomoRLowIP").getPropertyValue("text")
val2 = display.getWidget("TextInputTomoRHighIP").getPropertyValue("text")
val3 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxElectricR").getPV() ) ))
val4 = display.getWidget("TextInputElecRLowIP").getPropertyValue("text")
val5 = display.getWidget("TextInputElecRHighIP").getPropertyValue("text")
val6 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxMagneticR").getPV() ) ))
val7 = display.getWidget("TextInputMagRLowIP").getPropertyValue("text")
val8 = display.getWidget("TextInputMagRHighIP").getPropertyValue("text")
val9 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxCosineR").getPV() ) ))
val10 = display.getWidget("TextInputCosRLowIP").getPropertyValue("text")
val11 = display.getWidget("TextInputCosRHighIP").getPropertyValue("text")
val12 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxHIBDR").getPV() ) ))
val13 = display.getWidget("TextInputHIBDRLowIP").getPropertyValue("text")
val14 = display.getWidget("TextInputHIBDRHighIP").getPropertyValue("text")
val15 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxOPTMR").getPV() ) ))
val16 = display.getWidget("TextInputOPTMRLowIP").getPropertyValue("text")
val17 = display.getWidget("TextInputOPTMRHighIP").getPropertyValue("text")

val18 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomographyV").getPV() ) ))
val19 = display.getWidget("TextInputTomoVLowIP").getPropertyValue("text")
val20 = display.getWidget("TextInputTomoVHighIP").getPropertyValue("text")
val21 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxElectricV").getPV() ) ))
val22 = display.getWidget("TextInputElecVLowIP").getPropertyValue("text")
val23 = display.getWidget("TextInputElecVHighIP").getPropertyValue("text")
val24 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxMagneticV").getPV() ) ))
val25 = display.getWidget("TextInputMagVLowIP").getPropertyValue("text")
val26 = display.getWidget("TextInputMagVHighIP").getPropertyValue("text")
val27 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxSineV").getPV() ) ))
val28 = display.getWidget("TextInputSinVLowIP").getPropertyValue("text")
val29 = display.getWidget("TextInputSinVHighIP").getPropertyValue("text")
val30 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxHIBDV").getPV() ) ))
val31 = display.getWidget("TextInputHIBDVLowIP").getPropertyValue("text")
val32 = display.getWidget("TextInputHIBDVHighIP").getPropertyValue("text")
val33 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxOPTMV").getPV() ) ))
val34 = display.getWidget("TextInputOPTMVLowIP").getPropertyValue("text")
val35 = display.getWidget("TextInputOPTMVHighIP").getPropertyValue("text")

val36 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxUseInterferometry").getPV() ) ))
val37 = display.getWidget("TextInputIPTreshold").getPropertyValue("text")

val38 = display.getWidget("TextInputPSoftPrimaryPS").getPropertyValue("text")
val39 = display.getWidget("TextInputISoftPrimaryPS").getPropertyValue("text")
val40 = display.getWidget("TextInputDSoftPrimaryPS").getPropertyValue("text")
val41 = display.getWidget("TextInputPMedPrimaryPS").getPropertyValue("text")
val42 = display.getWidget("TextInputIMedPrimaryPS").getPropertyValue("text")
val43 = display.getWidget("TextInputDMedPrimaryPS").getPropertyValue("text")
val44 = display.getWidget("TextInputPHardPrimaryPS").getPropertyValue("text")
val45 = display.getWidget("TextInputIHardPrimaryPS").getPropertyValue("text")
val46 = display.getWidget("TextInputDHardPrimaryPS").getPropertyValue("text")
val47 = display.getWidget("TextInputPSoftVerticalPS").getPropertyValue("text")
val48 = display.getWidget("TextInputISoftVerticalPS").getPropertyValue("text")
val49 = display.getWidget("TextInputDSoftVerticalPS").getPropertyValue("text")
val50 = display.getWidget("TextInputPMedVerticalPS").getPropertyValue("text")
val51 = display.getWidget("TextInputIMedVerticalPS").getPropertyValue("text")
val52 = display.getWidget("TextInputDMedVerticalPS").getPropertyValue("text")
val53 = display.getWidget("TextInputPHardVerticalPS").getPropertyValue("text")
val54 = display.getWidget("TextInputIHardVerticalPS").getPropertyValue("text")
val55 = display.getWidget("TextInputDHardVerticalPS").getPropertyValue("text")
val56 = display.getWidget("TextInputPSoftHorizontalPS").getPropertyValue("text")
val57 = display.getWidget("TextInputISoftHorizontalPS").getPropertyValue("text")
val58 = display.getWidget("TextInputDSoftHorizontalPS").getPropertyValue("text")
val59 = display.getWidget("TextInputPMedHorizontalPS").getPropertyValue("text")
val60 = display.getWidget("TextInputIMedHorizontalPS").getPropertyValue("text")
val61 = display.getWidget("TextInputDMedHorizontalPS").getPropertyValue("text")
val62 = display.getWidget("TextInputPHardHorizontalPS").getPropertyValue("text")
val63 = display.getWidget("TextInputIHardHorizontalPS").getPropertyValue("text")
val64 = display.getWidget("TextInputDHardHorizontalPS").getPropertyValue("text")

val65 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxAutoBreak").getPV() ) ))

val66 = display.getWidget("TextInputDischNCycles").getPropertyValue("text")
val67 = display.getWidget("TextInputDischTime").getPropertyValue("text")
val68 = display.getWidget("TextInputMARTECycle").getPropertyValue("text")
val69 = display.getWidget("TextInputStartupDelay").getPropertyValue("text")

val70 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe01").getPV() ) ))
val71 = display.getWidget("TextInputProbe01Angle").getPropertyValue("text")
val72 = display.getWidget("TextInputProbe01Calib").getPropertyValue("text")
val73 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe02").getPV() ) ))
val74 = display.getWidget("TextInputProbe02Angle").getPropertyValue("text")
val75 = display.getWidget("TextInputProbe02Calib").getPropertyValue("text")
val76 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe03").getPV() ) ))
val77 = display.getWidget("TextInputProbe03Angle").getPropertyValue("text")
val78 = display.getWidget("TextInputProbe03Calib").getPropertyValue("text")
val79 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe04").getPV() ) ))
val80 = display.getWidget("TextInputProbe04Angle").getPropertyValue("text")
val81 = display.getWidget("TextInputProbe04Calib").getPropertyValue("text")
val82 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe05").getPV() ) ))
val83 = display.getWidget("TextInputProbe05Angle").getPropertyValue("text")
val84 = display.getWidget("TextInputProbe05Calib").getPropertyValue("text")
val85 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe06").getPV() ) ))
val86 = display.getWidget("TextInputProbe06Angle").getPropertyValue("text")
val87 = display.getWidget("TextInputProbe06Calib").getPropertyValue("text")
val88 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe07").getPV() ) ))
val89 = display.getWidget("TextInputProbe07Angle").getPropertyValue("text")
val90 = display.getWidget("TextInputProbe07Calib").getPropertyValue("text")
val91 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe08").getPV() ) ))
val92 = display.getWidget("TextInputProbe08Angle").getPropertyValue("text")
val93 = display.getWidget("TextInputProbe08Calib").getPropertyValue("text")
val94 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe09").getPV() ) ))
val95 = display.getWidget("TextInputProbe09Angle").getPropertyValue("text")
val96 = display.getWidget("TextInputProbe09Calib").getPropertyValue("text")
val97 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe10").getPV() ) ))
val98 = display.getWidget("TextInputProbe10Angle").getPropertyValue("text")
val99 = display.getWidget("TextInputProbe10Calib").getPropertyValue("text")
val100 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe11").getPV() ) ))
val101 = display.getWidget("TextInputProbe11Angle").getPropertyValue("text")
val102 = display.getWidget("TextInputProbe11Calib").getPropertyValue("text")
val103 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxProbe12").getPV() ) ))
val104 = display.getWidget("TextInputProbe12Angle").getPropertyValue("text")
val105 = display.getWidget("TextInputProbe12Calib").getPropertyValue("text")

val106 = PVUtil.getString( display.getWidget("RadioBoxPosNeg").getPV() )

val107 = display.getWidget("TextInputPosT1").getPropertyValue("text")
val108 = display.getWidget("TextInputPosT2").getPropertyValue("text")
val109 = display.getWidget("TextInputPosT3").getPropertyValue("text")
val110 = display.getWidget("TextInputPosT4").getPropertyValue("text")
val111 = display.getWidget("TextInputPosT5").getPropertyValue("text")
val112 = display.getWidget("TextInputPosT6").getPropertyValue("text")
val113 = display.getWidget("TextInputPosT7").getPropertyValue("text")

val114 = PVUtil.getString( display.getWidget("ComboBoxPosPrimaryT1").getPV() )
val115 = PVUtil.getString( display.getWidget("ComboBoxPosVerticalT1").getPV() )
val116 = PVUtil.getString( display.getWidget("ComboBoxPosHorizontalT1").getPV() )
val117 = PVUtil.getString( display.getWidget("ComboBoxPosPrimaryT2").getPV() )
val118 = PVUtil.getString( display.getWidget("ComboBoxPosVerticalT2").getPV() )
val119 = PVUtil.getString( display.getWidget("ComboBoxPosHorizontalT2").getPV() )
val120 = PVUtil.getString( display.getWidget("ComboBoxPosPrimaryT3").getPV() )
val121 = PVUtil.getString( display.getWidget("ComboBoxPosVerticalT3").getPV() )
val122 = PVUtil.getString( display.getWidget("ComboBoxPosHorizontalT3").getPV() )
val123 = PVUtil.getString( display.getWidget("ComboBoxPosPrimaryT4").getPV() )
val124 = PVUtil.getString( display.getWidget("ComboBoxPosVerticalT4").getPV() )
val125 = PVUtil.getString( display.getWidget("ComboBoxPosHorizontalT4").getPV() )
val126 = PVUtil.getString( display.getWidget("ComboBoxPosPrimaryT5").getPV() )
val127 = PVUtil.getString( display.getWidget("ComboBoxPosVerticalT5").getPV() )
val128 = PVUtil.getString( display.getWidget("ComboBoxPosHorizontalT5").getPV() )
val129 = PVUtil.getString( display.getWidget("ComboBoxPosPrimaryT6").getPV() )
val130 = PVUtil.getString( display.getWidget("ComboBoxPosVerticalT6").getPV() )
val131 = PVUtil.getString( display.getWidget("ComboBoxPosHorizontalT6").getPV() )
val132 = PVUtil.getString( display.getWidget("ComboBoxPosPrimaryT7").getPV() )
val133 = PVUtil.getString( display.getWidget("ComboBoxPosVerticalT7").getPV() )
val134 = PVUtil.getString( display.getWidget("ComboBoxPosHorizontalT7").getPV() )

val135 = display.getWidget("TextInputNegT1").getPropertyValue("text")
val136 = display.getWidget("TextInputNegT2").getPropertyValue("text")
val137 = display.getWidget("TextInputNegT3").getPropertyValue("text")
val138 = display.getWidget("TextInputNegT4").getPropertyValue("text")
val139 = display.getWidget("TextInputNegT5").getPropertyValue("text")
val140 = display.getWidget("TextInputNegT6").getPropertyValue("text")
val141 = display.getWidget("TextInputNegT7").getPropertyValue("text")

val142 = PVUtil.getString( display.getWidget("ComboBoxNegPrimaryT1").getPV() )
val143 = PVUtil.getString( display.getWidget("ComboBoxNegVerticalT1").getPV() )
val144 = PVUtil.getString( display.getWidget("ComboBoxNegHorizontalT1").getPV() )
val145 = PVUtil.getString( display.getWidget("ComboBoxNegPrimaryT2").getPV() )
val146 = PVUtil.getString( display.getWidget("ComboBoxNegVerticalT2").getPV() )
val147 = PVUtil.getString( display.getWidget("ComboBoxNegHorizontalT2").getPV() )
val148 = PVUtil.getString( display.getWidget("ComboBoxNegPrimaryT3").getPV() )
val149 = PVUtil.getString( display.getWidget("ComboBoxNegVerticalT3").getPV() )
val150 = PVUtil.getString( display.getWidget("ComboBoxNegHorizontalT3").getPV() )
val151 = PVUtil.getString( display.getWidget("ComboBoxNegPrimaryT4").getPV() )
val152 = PVUtil.getString( display.getWidget("ComboBoxNegVerticalT4").getPV() )
val153 = PVUtil.getString( display.getWidget("ComboBoxNegHorizontalT4").getPV() )
val154 = PVUtil.getString( display.getWidget("ComboBoxNegPrimaryT5").getPV() )
val155 = PVUtil.getString( display.getWidget("ComboBoxNegVerticalT5").getPV() )
val156 = PVUtil.getString( display.getWidget("ComboBoxNegHorizontalT5").getPV() )
val157 = PVUtil.getString( display.getWidget("ComboBoxNegPrimaryT6").getPV() )
val158 = PVUtil.getString( display.getWidget("ComboBoxNegVerticalT6").getPV() )
val159 = PVUtil.getString( display.getWidget("ComboBoxNegHorizontalT6").getPV() )
val160 = PVUtil.getString( display.getWidget("ComboBoxNegPrimaryT7").getPV() )
val161 = PVUtil.getString( display.getWidget("ComboBoxNegVerticalT7").getPV() )
val162 = PVUtil.getString( display.getWidget("ComboBoxNegHorizontalT7").getPV() )

val163 = display.getWidget("TextInputBasicFileDescription").getPropertyValue("text")

val164 = PVUtil.getString( display.getWidget("ComboBoxBWaveType").getPV() )
val165 = display.getWidget("TextInputBWaveXXG").getPropertyValue("text")
val166 = display.getWidget("TextInputBWaveYYG").getPropertyValue("text")

#Advanced Mode
val167 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoTopChn1").getPV() ) ))
val168 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoTopChn2").getPV() ) ))
val169 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoTopChn3").getPV() ) ))
val170 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoTopChn4").getPV() ) ))
val171 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoTopChn5").getPV() ) ))
val172 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoTopChn6").getPV() ) ))
val173 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoTopChn7").getPV() ) ))
val174 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoTopChn8").getPV() ) ))
val175 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoOutterChn1").getPV() ) ))
val176 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoOutterChn2").getPV() ) ))
val177 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoOutterChn3").getPV() ) ))
val178 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoOutterChn4").getPV() ) ))
val179 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoOutterChn5").getPV() ) ))
val180 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoOutterChn6").getPV() ) ))
val181 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoOutterChn7").getPV() ) ))
val182 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoOutterChn8").getPV() ) ))
val183 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoBottomChn1").getPV() ) ))
val184 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoBottomChn2").getPV() ) ))
val185 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoBottomChn3").getPV() ) ))
val186 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoBottomChn4").getPV() ) ))
val187 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoBottomChn5").getPV() ) ))
val188 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoBottomChn6").getPV() ) ))
val189 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoBottomChn7").getPV() ) ))
val190 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxTomoBottomChn8").getPV() ) ))

val191 = display.getWidget("TextInputPrimaryUartPortAddress").getPropertyValue("text")
val192 = display.getWidget("TextInputPrimaryZeroCurrentPoint").getPropertyValue("text")
val193 = display.getWidget("TextInputPrimaryCurrentSetup").getPropertyValue("text")
val194 = display.getWidget("TextInputVerticalUartPortAddress").getPropertyValue("text")
val195 = display.getWidget("TextInputVerticalZeroCurrentPoint").getPropertyValue("text")
val196 = display.getWidget("TextInputVerticalCurrentSetup").getPropertyValue("text")
val197 = display.getWidget("TextInputHorizontalUartPortAddress").getPropertyValue("text")
val198 = display.getWidget("TextInputHorizontalZeroCurrentPoint").getPropertyValue("text")
val199 = display.getWidget("TextInputHorizontalCurrentSetup").getPropertyValue("text")

val200 = display.getWidget("dialogFilePathControl").getPropertyValue("text")
val201 = display.getWidget("dialogFilePathTomo").getPropertyValue("text")

val202 = display.getWidget("TextInputToroidalCurrentMin").getPropertyValue("text")
val203 = display.getWidget("TextInputToroidalCurrentMax").getPropertyValue("text")
val204 = display.getWidget("TextInputPrimaryCurrentMin").getPropertyValue("text")
val205 = display.getWidget("TextInputPrimaryCurrentMax").getPropertyValue("text")
val206 = display.getWidget("TextInputVerticalCurrentMin").getPropertyValue("text")
val207 = display.getWidget("TextInputVerticalCurrentMax").getPropertyValue("text")
val208 = display.getWidget("TextInputHorizontalCurrentMin").getPropertyValue("text")
val209 = display.getWidget("TextInputHorizontalCurrentMax").getPropertyValue("text")
val210 = display.getWidget("TextInputPlasmaCurrentMin").getPropertyValue("text")
val211 = display.getWidget("TextInputPlasmaCurrentMax").getPropertyValue("text")
val212 = display.getWidget("TextInputRadialPositionMin").getPropertyValue("text")
val213 = display.getWidget("TextInputRadialPositionMax").getPropertyValue("text")
val214 = display.getWidget("TextInputVerticalPositionMin").getPropertyValue("text")
val215 = display.getWidget("TextInputVerticalPositionMax").getPropertyValue("text")
val216 = display.getWidget("TextInputDensityAlphaMin").getPropertyValue("text")
val217 = display.getWidget("TextInputDensityAlphaMax").getPropertyValue("text")

val218 = display.getWidget("TextInputPuffingDuration").getPropertyValue("text")
val219 = display.getWidget("TextInputMaximumIdleTime").getPropertyValue("text")
val220 = display.getWidget("TextInputMinimumIdleTime").getPropertyValue("text")
val221 = display.getWidget("TextInputPercentageCycleChange").getPropertyValue("text")

val222 = PVUtil.getString( display.getWidget("RadioBoxDensityAlpha").getPV() )

val223 = display.getWidget("TextInputThreadPriority").getPropertyValue("text")
val224 = display.getWidget("TextInputRunOnCPUs").getPropertyValue("text")

val225 = str(int(PVUtil.getDouble( display.getWidget("CheckBoxUnsuccessfullBreakdown").getPV() ) ))

val226 = display.getWidget("TextInputSaturationPredictor1").getPropertyValue("text")
val227 = display.getWidget("TextInputSaturationIPrimaryVLoop").getPropertyValue("text")

val228 = display.getWidget("TextInputOnlineDischTime").getPropertyValue("text")
val229 = display.getWidget("TextInputBreakdownMaximumTime").getPropertyValue("text")
val230 = display.getWidget("TextInputInversionMaximumTime").getPropertyValue("text")

val231 = PVUtil.getString( display.getWidget("RadioBoxPuffingOutput").getPV() )

val232 = display.getWidget("TextInputAdvancedFileDescription").getPropertyValue("text")

val233 = PVUtil.getString( display.getWidget("ComboBoxAWaveType").getPV() )
val234 = display.getWidget("TextInputAWaveXXG").getPropertyValue("text")
val235 = display.getWidget("TextInputAWaveYYG").getPropertyValue("text")

filename2 = "/home/opertok/CSS-Workspaces/sys-mng-opi"+display.getWidget("dialogFilePath2").getPropertyValue("text")
myfile = open(filename2, 'w')
myfile.write('CheckBoxTomographyR\t')
myfile.write(val0)
myfile.write('\nTextInputTomoRLowIP\t')
myfile.write(val1)
myfile.write('\nTextInputTomoRHighIP\t')
myfile.write(val2)
myfile.write('\nCheckBoxElectricR\t')
myfile.write(val3)
myfile.write('\nTextInputElecRLowIP\t')
myfile.write(val4)
myfile.write('\nTextInputElecRHighIP\t')
myfile.write(val5)
myfile.write('\nCheckBoxMagneticR\t')
myfile.write(val6)
myfile.write('\nTextInputMagRLowIP\t')
myfile.write(val7)
myfile.write('\nTextInputMagRHighIP\t')
myfile.write(val8)
myfile.write('\nCheckBoxCosineR\t')
myfile.write(val9)
myfile.write('\nTextInputCosRLowIP\t')
myfile.write(val10)
myfile.write('\nTextInputCosRHighIP\t')
myfile.write(val11)
myfile.write('\nCheckBoxHIBDR\t')
myfile.write(val12)
myfile.write('\nTextInputHIBDRLowIP\t')
myfile.write(val13)
myfile.write('\nTextInputHIBDRHighIP\t')
myfile.write(val14)
myfile.write('\nCheckBoxOPTMR\t')
myfile.write(val15)
myfile.write('\nTextInputOPTMRLowIP\t')
myfile.write(val16)
myfile.write('\nTextInputOPTMRHighIP\t')
myfile.write(val17)
myfile.write('\nCheckBoxTomographyV\t')
myfile.write(val18)
myfile.write('\nTextInputTomoVLowIP\t')
myfile.write(val19)
myfile.write('\nTextInputTomoVHighIP\t')
myfile.write(val20)
myfile.write('\nCheckBoxElectricV\t')
myfile.write(val21)
myfile.write('\nTextInputElecVLowIP\t')
myfile.write(val22)
myfile.write('\nTextInputElecVHighIP\t')
myfile.write(val23)
myfile.write('\nCheckBoxMagneticV\t')
myfile.write(val24)
myfile.write('\nTextInputMagVLowIP\t')
myfile.write(val25)
myfile.write('\nTextInputMagVHighIP\t')
myfile.write(val26)
myfile.write('\nCheckBoxSineV\t')
myfile.write(val27)
myfile.write('\nTextInputSinVLowIP\t')
myfile.write(val28)
myfile.write('\nTextInputSinVHighIP\t')
myfile.write(val29)
myfile.write('\nCheckBoxHIBDV\t')
myfile.write(val30)
myfile.write('\nTextInputHIBDVLowIP\t')
myfile.write(val31)
myfile.write('\nTextInputHIBDVHighIP\t')
myfile.write(val32)
myfile.write('\nCheckBoxOPTMV\t')
myfile.write(val33)
myfile.write('\nTextInputOPTMVLowIP\t')
myfile.write(val34)
myfile.write('\nTextInputOPTMVHighIP\t')
myfile.write(val35)
myfile.write('\nCheckBoxUseInterferometry\t')
myfile.write(val36)
myfile.write('\nTextInputIPTreshold\t')
myfile.write(val37)
myfile.write('\nTextInputPSoftPrimaryPS\t')
myfile.write(val38)
myfile.write('\nTextInputISoftPrimaryPS\t')
myfile.write(val39)
myfile.write('\nTextInputDSoftPrimaryPS\t')
myfile.write(val40)
myfile.write('\nTextInputPMedPrimaryPS\t')
myfile.write(val41)
myfile.write('\nTextInputIMedPrimaryPS\t')
myfile.write(val42)
myfile.write('\nTextInputDMedPrimaryPS\t')
myfile.write(val43)
myfile.write('\nTextInputPHardPrimaryPS\t')
myfile.write(val44)
myfile.write('\nTextInputIHardPrimaryPS\t')
myfile.write(val45)
myfile.write('\nTextInputDHardPrimaryPS\t')
myfile.write(val46)
myfile.write('\nTextInputPSoftVerticalPS\t')
myfile.write(val47)
myfile.write('\nTextInputISoftVerticalPS\t')
myfile.write(val48)
myfile.write('\nTextInputDSoftVerticalPS\t')
myfile.write(val49)
myfile.write('\nTextInputPMedVerticalPS\t')
myfile.write(val50)
myfile.write('\nTextInputIMedVerticalPS\t')
myfile.write(val51)
myfile.write('\nTextInputDMedVerticalPS\t')
myfile.write(val52)
myfile.write('\nTextInputPHardVerticalPS\t')
myfile.write(val53)
myfile.write('\nTextInputIHardVerticalPS\t')
myfile.write(val54)
myfile.write('\nTextInputDHardVerticalPS\t')
myfile.write(val55)
myfile.write('\nTextInputPSoftHorizontalPS\t')
myfile.write(val56)
myfile.write('\nTextInputISoftHorizontalPS\t')
myfile.write(val57)
myfile.write('\nTextInputDSoftHorizontalPS\t')
myfile.write(val58)
myfile.write('\nTextInputPMedHorizontalPS\t')
myfile.write(val59)
myfile.write('\nTextInputIMedHorizontalPS\t')
myfile.write(val60)
myfile.write('\nTextInputDMedHorizontalPS\t')
myfile.write(val61)
myfile.write('\nTextInputPHardHorizontalPS\t')
myfile.write(val62)
myfile.write('\nTextInputIHardHorizontalPS\t')
myfile.write(val63)
myfile.write('\nTextInputDHardHorizontalPS\t')
myfile.write(val64)
myfile.write('\nCheckBoxAutoBreak\t')
myfile.write(val65)
myfile.write('\nTextInputDischNCycles\t')
myfile.write(val66)
myfile.write('\nTextInputDischTime\t')
myfile.write(val67)
myfile.write('\nTextInputMARTECycle\t')
myfile.write(val68)
myfile.write('\nTextInputStartupDelay\t')
myfile.write(val69)
myfile.write('\nCheckBoxProbe01\t')
myfile.write(val70)
myfile.write('\nTextInputProbe01Angle\t')
myfile.write(val71)
myfile.write('\nTextInputProbe01Calib\t')
myfile.write(val72)
myfile.write('\nCheckBoxProbe02\t')
myfile.write(val73)
myfile.write('\nTextInputProbe02Angle\t')
myfile.write(val74)
myfile.write('\nTextInputProbe02Calib\t')
myfile.write(val75)
myfile.write('\nCheckBoxProbe03\t')
myfile.write(val76)
myfile.write('\nTextInputProbe03Angle\t')
myfile.write(val77)
myfile.write('\nTextInputProbe03Calib\t')
myfile.write(val78)
myfile.write('\nCheckBoxProbe04\t')
myfile.write(val79)
myfile.write('\nTextInputProbe04Angle\t')
myfile.write(val80)
myfile.write('\nTextInputProbe04Calib\t')
myfile.write(val81)
myfile.write('\nCheckBoxProbe05\t')
myfile.write(val82)
myfile.write('\nTextInputProbe05Angle\t')
myfile.write(val83)
myfile.write('\nTextInputProbe05Calib\t')
myfile.write(val84)
myfile.write('\nCheckBoxProbe06\t')
myfile.write(val85)
myfile.write('\nTextInputProbe06Angle\t')
myfile.write(val86)
myfile.write('\nTextInputProbe06Calib\t')
myfile.write(val87)
myfile.write('\nCheckBoxProbe07\t')
myfile.write(val88)
myfile.write('\nTextInputProbe07Angle\t')
myfile.write(val89)
myfile.write('\nTextInputProbe07Calib\t')
myfile.write(val90)
myfile.write('\nCheckBoxProbe08\t')
myfile.write(val91)
myfile.write('\nTextInputProbe08Angle\t')
myfile.write(val92)
myfile.write('\nTextInputProbe08Calib\t')
myfile.write(val93)
myfile.write('\nCheckBoxProbe09\t')
myfile.write(val94)
myfile.write('\nTextInputProbe09Angle\t')
myfile.write(val95)
myfile.write('\nTextInputProbe09Calib\t')
myfile.write(val96)
myfile.write('\nCheckBoxProbe10\t')
myfile.write(val97)
myfile.write('\nTextInputProbe10Angle\t')
myfile.write(val98)
myfile.write('\nTextInputProbe10Calib\t')
myfile.write(val99)
myfile.write('\nCheckBoxProbe11\t')
myfile.write(val100)
myfile.write('\nTextInputProbe11Angle\t')
myfile.write(val101)
myfile.write('\nTextInputProbe11Calib\t')
myfile.write(val102)
myfile.write('\nCheckBoxProbe12\t')
myfile.write(val103)
myfile.write('\nTextInputProbe12Angle\t')
myfile.write(val104)
myfile.write('\nTextInputProbe12Calib\t')
myfile.write(val105)
myfile.write('\nRadioBoxPosNeg\t')
myfile.write(val106)
myfile.write('\nTextInputPosT1\t')
myfile.write(val107)
myfile.write('\nTextInputPosT2\t')
myfile.write(val108)
myfile.write('\nTextInputPosT3\t')
myfile.write(val109)
myfile.write('\nTextInputPosT4\t')
myfile.write(val110)
myfile.write('\nTextInputPosT5\t')
myfile.write(val111)
myfile.write('\nTextInputPosT6\t')
myfile.write(val112)
myfile.write('\nTextInputPosT7\t')
myfile.write(val113)
myfile.write('\nComboBoxPosPrimaryT1\t')
myfile.write(val114)
myfile.write('\nComboBoxPosVerticalT1\t')
myfile.write(val115)
myfile.write('\nComboBoxPosHorizontalT1\t')
myfile.write(val116)
myfile.write('\nComboBoxPosPrimaryT2\t')
myfile.write(val117)
myfile.write('\nComboBoxPosVerticalT2\t')
myfile.write(val118)
myfile.write('\nComboBoxPosHorizontalT2\t')
myfile.write(val119)
myfile.write('\nComboBoxPosPrimaryT3\t')
myfile.write(val120)
myfile.write('\nComboBoxPosVerticalT3\t')
myfile.write(val121)
myfile.write('\nComboBoxPosHorizontalT3\t')
myfile.write(val122)
myfile.write('\nComboBoxPosPrimaryT4\t')
myfile.write(val123)
myfile.write('\nComboBoxPosVerticalT4\t')
myfile.write(val124)
myfile.write('\nComboBoxPosHorizontalT4\t')
myfile.write(val125)
myfile.write('\nComboBoxPosPrimaryT5\t')
myfile.write(val126)
myfile.write('\nComboBoxPosVerticalT5\t')
myfile.write(val127)
myfile.write('\nComboBoxPosHorizontalT5\t')
myfile.write(val128)
myfile.write('\nComboBoxPosPrimaryT6\t')
myfile.write(val129)
myfile.write('\nComboBoxPosVerticalT6\t')
myfile.write(val130)
myfile.write('\nComboBoxPosHorizontalT6\t')
myfile.write(val131)
myfile.write('\nComboBoxPosPrimaryT7\t')
myfile.write(val132)
myfile.write('\nComboBoxPosVerticalT7\t')
myfile.write(val133)
myfile.write('\nComboBoxPosPrimaryT7\t')
myfile.write(val134)
myfile.write('\nTextInputNegT1\t')
myfile.write(val135)
myfile.write('\nTextInputNegT2\t')
myfile.write(val136)
myfile.write('\nTextInputNegT3\t')
myfile.write(val137)
myfile.write('\nTextInputNegT4\t')
myfile.write(val138)
myfile.write('\nTextInputNegT5\t')
myfile.write(val139)
myfile.write('\nTextInputNegT6\t')
myfile.write(val140)
myfile.write('\nTextInputNegT7\t')
myfile.write(val141)
myfile.write('\nComboBoxNegPrimaryT1\t')
myfile.write(val142)
myfile.write('\nComboBoxNegVerticalT1\t')
myfile.write(val143)
myfile.write('\nComboBoxNegHorizontalT1\t')
myfile.write(val144)
myfile.write('\nComboBoxNegPrimaryT2\t')
myfile.write(val145)
myfile.write('\nComboBoxNegVerticalT2\t')
myfile.write(val146)
myfile.write('\nComboBoxNegHorizontalT2\t')
myfile.write(val147)
myfile.write('\nComboBoxNegPrimaryT3\t')
myfile.write(val148)
myfile.write('\nComboBoxNegVerticalT3\t')
myfile.write(val149)
myfile.write('\nComboBoxNegHorizontalT3\t')
myfile.write(val150)
myfile.write('\nComboBoxNegPrimaryT4\t')
myfile.write(val151)
myfile.write('\nComboBoxNegVerticalT4\t')
myfile.write(val152)
myfile.write('\nComboBoxNegHorizontalT4\t')
myfile.write(val153)
myfile.write('\nComboBoxNegPrimaryT5\t')
myfile.write(val154)
myfile.write('\nComboBoxNegVerticalT5\t')
myfile.write(val155)
myfile.write('\nComboBoxNegHorizontalT5\t')
myfile.write(val156)
myfile.write('\nComboBoxNegPrimaryT6\t')
myfile.write(val157)
myfile.write('\nComboBoxNegVerticalT6\t')
myfile.write(val158)
myfile.write('\nComboBoxNegHorizontalT6\t')
myfile.write(val159)
myfile.write('\nComboBoxNegPrimaryT7\t')
myfile.write(val160)
myfile.write('\nComboBoxNegVerticalT7\t')
myfile.write(val161)
myfile.write('\nComboBoxNegHorizontalT7\t')
myfile.write(val162)
myfile.write('\nTextInputBasicFileDescription\t')
myfile.write(val163)
myfile.write('\nComboBoxBWaveType\t')
myfile.write(val164)
myfile.write('\nTextInputBWaveXXG\t')
myfile.write(val165)
myfile.write('\nTextInputBWaveYYG\t')
myfile.write(val166)
myfile.write('\nCheckBoxTomoTopChn1\t')
myfile.write(val167)
myfile.write('\nCheckBoxTomoTopChn2\t')
myfile.write(val168)
myfile.write('\nCheckBoxTomoTopChn3\t')
myfile.write(val169)
myfile.write('\nCheckBoxTomoTopChn4\t')
myfile.write(val170)
myfile.write('\nCheckBoxTomoTopChn5\t')
myfile.write(val171)
myfile.write('\nCheckBoxTomoTopChn6\t')
myfile.write(val172)
myfile.write('\nCheckBoxTomoTopChn7\t')
myfile.write(val173)
myfile.write('\nCheckBoxTomoTopChn8\t')
myfile.write(val174)
myfile.write('\nCheckBoxTomoOutterChn1\t')
myfile.write(val175)
myfile.write('\nCheckBoxTomoOutterChn2\t')
myfile.write(val176)
myfile.write('\nCheckBoxTomoOutterChn3\t')
myfile.write(val177)
myfile.write('\nCheckBoxTomoOutterChn4\t')
myfile.write(val178)
myfile.write('\nCheckBoxTomoOutterChn5\t')
myfile.write(val179)
myfile.write('\nCheckBoxTomoOutterChn6\t')
myfile.write(val180)
myfile.write('\nCheckBoxTomoOutterChn7\t')
myfile.write(val181)
myfile.write('\nCheckBoxTomoOutterChn8\t')
myfile.write(val182)
myfile.write('\nCheckBoxTomoBottomChn1\t')
myfile.write(val183)
myfile.write('\nCheckBoxTomoBottomChn2\t')
myfile.write(val184)
myfile.write('\nCheckBoxTomoBottomChn3\t')
myfile.write(val185)
myfile.write('\nCheckBoxTomoBottomChn4\t')
myfile.write(val186)
myfile.write('\nCheckBoxTomoBottomChn5\t')
myfile.write(val187)
myfile.write('\nCheckBoxTomoBottomChn6\t')
myfile.write(val188)
myfile.write('\nCheckBoxTomoBottomChn7\t')
myfile.write(val189)
myfile.write('\nCheckBoxTomoBottomChn8\t')
myfile.write(val190)
myfile.write('\nTextInputPrimaryUartPortAddress\t')
myfile.write(val191)
myfile.write('\nTextInputPrimaryZeroCurrentPoint\t')
myfile.write(val192)
myfile.write('\nTextInputPrimaryCurrentSetup\t')
myfile.write(val193)
myfile.write('\nTextInputVerticalUartPortAddress\t')
myfile.write(val194)
myfile.write('\nTextInputVerticalZeroCurrentPoint\t')
myfile.write(val195)
myfile.write('\nTextInputVerticalCurrentSetup\t')
myfile.write(val196)
myfile.write('\nTextInputHorizontalUartPortAddress\t')
myfile.write(val197)
myfile.write('\nTextInputHorizontalZeroCurrentPoint\t')
myfile.write(val198)
myfile.write('\nTextInputHorizontalCurrentSetup\t')
myfile.write(val199)
myfile.write('\ndialogFilePathControl\t')
myfile.write(val200)
myfile.write('\ndialogFilePathTomo\t')
myfile.write(val201)
myfile.write('\nTextInputToroidalCurrentMin\t')
myfile.write(val202)
myfile.write('\nTextInputToroidalCurrentMax\t')
myfile.write(val203)
myfile.write('\nTextInputPrimaryCurrentMin\t')
myfile.write(val204)
myfile.write('\nTextInputPrimaryCurrentMax\t')
myfile.write(val205)
myfile.write('\nTextInputVerticalCurrentMin\t')
myfile.write(val206)
myfile.write('\nTextInputVerticalCurrentMax\t')
myfile.write(val207)
myfile.write('\nTextInputHorizontalCurrentMin\t')
myfile.write(val208)
myfile.write('\nTextInputHorizontalCurrentMax\t')
myfile.write(val209)
myfile.write('\nTextInputPlasmaCurrentMin\t')
myfile.write(val210)
myfile.write('\nTextInputPlasmaCurrentMax\t')
myfile.write(val211)
myfile.write('\nTextInputRadialPositionMin\t')
myfile.write(val212)
myfile.write('\nTextInputRadialPositionMax\t')
myfile.write(val213)
myfile.write('\nTextInputVerticalPositionMin\t')
myfile.write(val214)
myfile.write('\nTextInputVerticalPositionMax\t')
myfile.write(val215)
myfile.write('\nTextInputDensityAlphaMin\t')
myfile.write(val216)
myfile.write('\nTextInputDensityAlphaMax\t')
myfile.write(val217)
myfile.write('\nTextInputPuffingDuration\t')
myfile.write(val218)
myfile.write('\nTextInputMaximumIdleTime\t')
myfile.write(val219)
myfile.write('\nTextInputMinimumIdleTime\t')
myfile.write(val220)
myfile.write('\nTextInputPercentageCycleChange\t')
myfile.write(val221)
myfile.write('\nRadioBoxDensityAlpha\t')
myfile.write(val222)
myfile.write('\nTextInputThreadPriority\t')
myfile.write(val223)
myfile.write('\nTextInputRunOnCPUs\t')
myfile.write(val224)
myfile.write('\nCheckBoxUnsuccessfullBreakdown\t')
myfile.write(val225)
myfile.write('\nTextInputSaturationPredictor1\t')
myfile.write(val226)
myfile.write('\nTextInputSaturationIPrimaryVLoop\t')
myfile.write(val227)
myfile.write('\nTextInputOnlineDischTime\t')
myfile.write(val228)
myfile.write('\nTextInputBreakdownMaximumTime\t')
myfile.write(val229)
myfile.write('\nTextInputInversionMaximumTime\t')
myfile.write(val230)
myfile.write('\nRadioBoxPuffingOutput\t')
myfile.write(val231)
myfile.write('\nTextInputAdvancedFileDescription\t')
myfile.write(val232)
myfile.write('\nComboBoxAWaveType\t')
myfile.write(val233)
myfile.write('\nTextInputAWaveXXG\t')
myfile.write(val234)
myfile.write('\nTextInputAWaveYYG\t')
myfile.write(val235)
myfile.write('\n')
myfile.close()
display.getWidget("ActionButtonTemplate_1").executeAction(1)