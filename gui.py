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
        rpm = int(self.ent[self.ID_ENGINERPM].get(), base=10)
        rpm = rpm + 1
        self.device.setEngineRPM(rpm)
        self.ent[self.ID_ENGINERPM].delete(0, END)
        self.ent[self.ID_ENGINERPM].insert(0, rpm)

    def cmdDecreaseEngineRPM(self):
        rpm = int(self.ent[self.ID_ENGINERPM].get(), base=10)
        rpm = rpm - 1
        self.device.setEngineRPM(rpm)
        self.ent[self.ID_ENGINERPM].delete(0, END)
        self.ent[self.ID_ENGINERPM].insert(0, rpm)

    def cmdSetEngineRPM(self):
        rpm = self.ent[self.ID_ENGINERPM].get()
        self.device.setEngineRPM(int(rpm, base=10))


    def cmdSetVehicleSpeed(self):
        speed = self.ent[self.ID_VEHICLESPEED].get()
        self.device.setVehicleSpeed(int(speed, 10))

    def cmdSetThrottlePosition(self):
        throttle = self.ent[self.ID_THROTTLEPOSITION].get()
        self.device.setThrottlePosition(int(throttle, 10))
    
    def cmdSetFuelLevelInput(self):
        level = self.ent[self.ID_FUELLEVELINPUT].get()
        self.device.setFuelLevelInput(int(level, 10))
    
    def cmdSetEngineFuelRate(self):
        rate = self.ent[self.ID_ENGINEFUELRATE].get()
        self.device.setEngineFuelRate(int(rate, 10))
    
    def cmdSetMAFAirFlowRate(self):
        rate = self.ent[self.ID_MAFAIRFLOWRATE].get()
        self.device.setMAFAirFlowRate(int(rate, 10))
    
    def cmdSetCalculatedEngineLoad(self):
        load = self.ent[self.ID_CALCULATEDENGINELOAD].get()
        self.device.setCalculatedEngineLoad(int(load, 10))


    def cmdTest(self):
        print "test"
        obd.main()
        
        

    def callback(self):
        print "Callback!"

    
    def createWidgets(self):
        self.paramControl(self.ID_ENGINERPM,            "EngineRPM",              self.cmdSetEngineRPM,            self.cmdDecreaseEngineRPM,       self.cmdIncreaseEngineRPM,       2, 1)
        self.paramControl(self.ID_VEHICLESPEED,         "Vehicle Speed",          self.cmdSetVehicleSpeed,         self.cmdSetVehicleSpeed,         self.cmdSetVehicleSpeed,         3, 1)        
        self.paramControl(self.ID_THROTTLEPOSITION,     "Throttle",               self.cmdSetThrottlePosition,     self.cmdDecreaseEngineRPM,       self.cmdIncreaseEngineRPM,       4, 1)
        self.paramControl(self.ID_FUELLEVELINPUT,       "Fuel Level Input",       self.cmdSetFuelLevelInput,       self.cmdDecreaseEngineRPM,       self.cmdIncreaseEngineRPM,       5, 1)
        self.paramControl(self.ID_ENGINEFUELRATE,       "Engine Fuel Rate",       self.cmdSetEngineFuelRate,       self.cmdSetEngineFuelRate,       self.cmdSetEngineFuelRate,       6, 1)
        self.paramControl(self.ID_MAFAIRFLOWRATE,       "MAF Air Flow Rate",      self.cmdSetMAFAirFlowRate,       self.cmdSetMAFAirFlowRate,       self.cmdSetMAFAirFlowRate,       7, 1)
        self.paramControl(self.ID_CALCULATEDENGINELOAD, "Calculated Engine Load", self.cmdSetCalculatedEngineLoad, self.cmdSetCalculatedEngineLoad, self.cmdSetCalculatedEngineLoad, 8, 1)
        
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

