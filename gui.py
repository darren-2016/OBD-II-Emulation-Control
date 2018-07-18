############################################################
# OBD-II Emulator Control Application
# 
# Module: GUI.py
#

import Tkinter
from Tkinter import *
import obd

#window=Tk()

print "GUI"

        

class Application(Frame):
    lbl    = [None] * 20
    ent    = [None] * 20
    btnSet = [None] * 20
    btnDec = [None] * 20
    btnInc = [None] * 20

    ID_ENGINERPM = 1
    ID_VEHICLESPEED = 2
    ID_THROTTLEPOSITION = 3
    ID_FUELLEVELINPUT = 4
    ID_ENGINEFUELRATE = 5
    ID_MAFAIRFLOWRATE = 6
    ID_CALCULATEDENGINELOAD = 7

    paramValue = [None] * 20

    paramValue[ID_ENGINERPM] = 0
    paramValue[ID_VEHICLESPEED] = 0
    paramValue[ID_THROTTLEPOSITION] = 0
    paramValue[ID_FUELLEVELINPUT] = 0
    paramValue[ID_ENGINEFUELRATE] = 0
    paramValue[ID_MAFAIRFLOWRATE] = 0
    paramValue[ID_CALCULATEDENGINELOAD] = 0

    SET = 1
    INC = 2
    DEC = 3


    
    def paramControl(self, index, label, callback, callbackDecParameter, callbackIncParameter, row, column):
        print "Label = " + label
        self.label = label
        self.callback = callback

        # Parameter Label
        self.lbl[index] = Label(self)
        self.lbl[index]["text"] = self.label
        self.lbl[index].grid(sticky="W", row=row, column=column)

        # Parameter Entry
        self.ent[index] = Entry(self, validate="focusout", validatecommand=callback)
        self.ent[index].grid(sticky="W", row=row, column=column+2)

        # Parameter Setting Apply Button
        self.btnSet[index] = Button(self)
        self.btnSet[index]["text"] = "Apply"
        self.btnSet[index]["command"] = callback
        self.btnSet[index].grid(sticky="W", row=row, column=column+4)
    
        # Parameter Decrement Button
        self.btnDec[index] = Button(self)
        self.btnDec[index]["text"] = "-"
        self.btnDec[index]["command"] = callbackDecParameter
        self.btnDec[index].grid(sticky="W", row=row, column=column+1)
        
        # Parameter Increment Button
        self.btnInc[index] = Button(self)
        self.btnInc[index]["text"] = "+"
        self.btnInc[index]["command"] = callbackIncParameter
        self.btnInc[index].grid(sticky="W", row=row, column=column+3)


    def initialiseParams(self):
        for i in range(self.ID_ENGINERPM, self.ID_CALCULATEDENGINELOAD + 1):
            self.ent[i].insert(0, self.paramValue[i])
        print


    def connectDevice(self):
        self.device.connectDevice()
    
    def closeDevice(self):
        self.device.closeConnection()


    def cmdIncreaseEngineRPM(self):
        self.cmdSetEngineRPM(self.INC)

    def cmdDecreaseEngineRPM(self):
        self.cmdSetEngineRPM(self.DEC)

    def cmdSetEngineRPM(self, mode=SET):
        rpm = int(self.ent[self.ID_ENGINERPM].get(), base=10)
        if mode == self.SET:
            self.device.setEngineRPM(rpm)
        if mode == self.INC:
            rpm = rpm + 1
            self.device.setEngineRPM(rpm)
            self.ent[self.ID_ENGINERPM].delete(0, END)
            self.ent[self.ID_ENGINERPM].insert(0, rpm)
        if mode == self.DEC:
            rpm = rpm - 1
            self.device.setEngineRPM(rpm)
            self.ent[self.ID_ENGINERPM].delete(0, END)
            self.ent[self.ID_ENGINERPM].insert(0, rpm)

    def cmdIncreaseVehicleSpeed(self):
        self.cmdSetVehicleSpeed(self.INC)

    def cmdDecreaseVehicleSpeed(self):
        self.cmdSetVehicleSpeed(self.DEC)

    def cmdSetVehicleSpeed(self, mode=SET):
        speed = int(self.ent[self.ID_VEHICLESPEED].get(), base=10)
        if mode == self.INC:
            speed = speed + 1
            self.ent[self.ID_VEHICLESPEED].delete(0, END)
            self.ent[self.ID_VEHICLESPEED].insert(0, speed)
        if mode == self.DEC:
            speed = speed - 1
            self.ent[self.ID_VEHICLESPEED].delete(0, END)
            self.ent[self.ID_VEHICLESPEED].insert(0, speed)
        self.device.setVehicleSpeed(speed)

    def cmdIncreaseThrottlePosition(self):
        self.cmdSetThrottlePosition(self.INC)

    def cmdDecreaseThrottlePosition(self):
        self.cmdSetThrottlePosition(self.DEC)

    def cmdSetThrottlePosition(self, mode=SET):
        throttle = int(self.ent[self.ID_THROTTLEPOSITION].get(), base=10)
        if mode == self.INC:
            throttle = throttle + 1
            self.ent[self.ID_THROTTLEPOSITION].delete(0, END)
            self.ent[self.ID_THROTTLEPOSITION].insert(0, throttle)
        if mode == self.DEC:
            throttle = throttle - 1
            self.ent[self.ID_THROTTLEPOSITION].delete(0, END)
            self.ent[self.ID_THROTTLEPOSITION].insert(0, throttle)
        self.device.setThrottlePosition(throttle)
    
    def cmdIncreaseFuelLevelInput(self):
        self.cmdSetFuelLevelInput(self.INC)

    def cmdDecreaseFuelLevelInput(self):
        self.cmdSetFuelLevelInput(self.DEC)

    def cmdSetFuelLevelInput(self, mode=SET):
        level = int(self.ent[self.ID_FUELLEVELINPUT].get(), base=10)
        if mode == self.INC:
            level = level + 1
            self.ent[self.ID_FUELLEVELINPUT].delete(0, END)
            self.ent[self.ID_FUELLEVELINPUT].insert(0, level)
        if mode == self.DEC:
            level = level - 1
            self.ent[self.ID_FUELLEVELINPUT].delete(0, END)
            self.ent[self.ID_FUELLEVELINPUT].insert(0, level)
        self.device.setFuelLevelInput(level)
    
    def cmdIncreaseEngineFuelRate(self):
        self.cmdSetEngineFuelRate(self.INC)

    def cmdDecreaseEngineFuelRate(self):
        self.cmdSetEngineFuelRate(self.DEC)

    def cmdSetEngineFuelRate(self, mode=SET):
        rate = int(self.ent[self.ID_ENGINEFUELRATE].get(), base=10)
        if mode == self.INC:
            rate = rate + 1
            self.ent[self.ID_ENGINEFUELRATE].delete(0, END)
            self.ent[self.ID_ENGINEFUELRATE].insert(0, rate)
        if mode == self.DEC:
            rate = rate - 1
            self.ent[self.ID_ENGINEFUELRATE].delete(0, END)
            self.ent[self.ID_ENGINEFUELRATE].insert(0, rate)
        self.device.setEngineFuelRate(rate)

    def cmdIncreaseMAFAirFlowRate(self):
        self.cmdSetMAFAirFlowRate(self.INC)

    def cmdDecreaseMAFAirFlowRate(self):
        self.cmdSetMAFAirFlowRate(self.DEC)

    def cmdSetMAFAirFlowRate(self, mode=SET):
        rate = int(self.ent[self.ID_MAFAIRFLOWRATE].get(),base=10)
        if mode == self.INC:
            rate = rate + 1
            self.ent[self.ID_MAFAIRFLOWRATE].delete(0, END)
            self.ent[self.ID_MAFAIRFLOWRATE].insert(0, rate)
        if mode == self.DEC:
            rate = rate - 1
            self.ent[self.ID_MAFAIRFLOWRATE].delete(0, END)
            self.ent[self.ID_MAFAIRFLOWRATE].insert(0, rate)
        self.device.setMAFAirFlowRate(rate)
    
    def cmdIncreaseCalculatedEngineLoad(self):
        self.cmdSetCalculatedEngineLoad(self.INC)

    def cmdDecreaseCalculatedEngineLoad(self):
        self.cmdSetCalculatedEngineLoad(self.DEC)

    def cmdSetCalculatedEngineLoad(self, mode=SET):
        load = int(self.ent[self.ID_CALCULATEDENGINELOAD].get(), base=10)
        if mode == self.INC:
            load = load + 1
            self.ent[self.ID_CALCULATEDENGINELOAD].delete(0, END)
            self.ent[self.ID_CALCULATEDENGINELOAD].insert(0, load)
        if mode == self.DEC:
            load = load - 1
            self.ent[self.ID_CALCULATEDENGINELOAD].delete(0, END)
            self.ent[self.ID_CALCULATEDENGINELOAD].insert(0, load)
        self.device.setCalculatedEngineLoad(load)


    def cmdTest(self):
        print "test"
        obd.main()
        
        

    def callback(self):
        print "Callback!"

    
    def createWidgets(self):
        self.paramControl(self.ID_ENGINERPM,            "EngineRPM",              self.cmdSetEngineRPM,            self.cmdDecreaseEngineRPM,            self.cmdIncreaseEngineRPM,            2, 1)
        self.paramControl(self.ID_VEHICLESPEED,         "Vehicle Speed",          self.cmdSetVehicleSpeed,         self.cmdDecreaseVehicleSpeed,         self.cmdIncreaseVehicleSpeed,         3, 1)        
        self.paramControl(self.ID_THROTTLEPOSITION,     "Throttle",               self.cmdSetThrottlePosition,     self.cmdDecreaseThrottlePosition,     self.cmdIncreaseThrottlePosition,     4, 1)
        self.paramControl(self.ID_FUELLEVELINPUT,       "Fuel Level Input",       self.cmdSetFuelLevelInput,       self.cmdDecreaseFuelLevelInput,       self.cmdIncreaseFuelLevelInput,       5, 1)
        self.paramControl(self.ID_ENGINEFUELRATE,       "Engine Fuel Rate",       self.cmdSetEngineFuelRate,       self.cmdDecreaseEngineFuelRate,       self.cmdIncreaseEngineFuelRate,       6, 1)
        self.paramControl(self.ID_MAFAIRFLOWRATE,       "MAF Air Flow Rate",      self.cmdSetMAFAirFlowRate,       self.cmdDecreaseMAFAirFlowRate,       self.cmdIncreaseMAFAirFlowRate,       7, 1)
        self.paramControl(self.ID_CALCULATEDENGINELOAD, "Calculated Engine Load", self.cmdSetCalculatedEngineLoad, self.cmdDecreaseCalculatedEngineLoad, self.cmdIncreaseCalculatedEngineLoad, 8, 1)
        
        self.btnQuit = Button(self)
        self.btnQuit["text"] = "QUIT"
        self.btnQuit["fg"]   = "red"
        self.btnQuit["command"] =  self.quit
        self.btnQuit.grid(row=1,column=3)

        self.btnConnectDevice = Button(self)
        self.btnConnectDevice["text"] = "Connect Device"
        self.btnConnectDevice["command"] = self.connectDevice
        self.btnConnectDevice.grid(row=1, column=1)

        self.btnClose = Button(self)
        self.btnClose["text"] = "Close"
        self.btnClose["fg"]   = "red"
        self.btnClose["command"] =  self.closeDevice
        self.btnClose.grid(row=1, column=2)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.device = obd.OBDEmulator()
        self.pack()
        self.createWidgets()
        self.initialiseParams()


root = Tk()
appVersion = "0.0.1"
root.wm_title('OBD-II Emulator Control ' + appVersion)
app = Application(master=root)
#root.configure(background='blue')
#app.configure(background='blue')
app.mainloop()
root.destroy()

