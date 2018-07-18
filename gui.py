# GUI.py
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
    
    def paramControl(self, index, label, callback, callbackDecParameter, callbackIncParameter, row, column):
        print "Label = " + label
        self.label = label
        self.callback = callback

        self.lbl[index] = Label(self)
        self.lbl[index]["text"] = self.label
        self.lbl[index].grid(sticky="W", row=row, column=column)

        self.ent[index] = Entry(self, validate="focusout", validatecommand=callback)
        self.ent[index].grid(sticky="W", row=row, column=column+2)

        self.btnSet[index] = Button(self)
        self.btnSet[index]["text"] = "Apply"
        self.btnSet[index]["command"] = callback
        self.btnSet[index].grid(sticky="W", row=row, column=column+4)
    
        self.btnDec[index] = Button(self)
        self.btnDec[index]["text"] = "-"
        self.btnDec[index]["command"] = callbackDecParameter
        self.btnDec[index].grid(sticky="W", row=row, column=column+1)
        
        self.btnInc[index] = Button(self)
        self.btnInc[index]["text"] = "+"
        self.btnInc[index]["command"] = callbackIncParameter
        self.btnInc[index].grid(sticky="W", row=row, column=column+3)


    def connectDevice(self):
        self.device.connectDevice()
    
    def closeDevice(self):
        self.device.closeConnection()

    def cmdIncreaseEngineRPM(self):
        self.device.setEngineRPM(1001)

    def cmdDecreaseEngineRPM(self):
        self.device.setEngineRPM(999)

    def cmdSetEngineRPM(self):
        rpm = self.entEngineRPM.get()
        self.device.setEngineRPM(int(rpm, base=10))

    def cmdSetVehicleSpeed(self):
        speed = self.entVehicleSpeed.get()
        self.device.setVehicleSpeed(int(speed, 10))

    def cmdSetThrottlePosition(self):
        throttle = self.entThrottlePosition.get()
        self.device.setThrottlePosition(int(throttle, 10))
    
    def cmdSetFuelLevelInput(self):
        level = self.entFuelLevelInput.get()
        self.device.setFuelLevelInput(int(level, 10))
    
    def cmdSetEngineFuelRate(self):
        rate = self.entEngineFuelRate.get()
        self.device.setEngineFuelRate(int(rate, 10))
    
    def cmdSetMAFAirFlowRate(self):
        rate = self.entMAFAirFlowRate.get()
        self.device.setMAFAirFlowRate(int(rate, 10))
    
    def cmdSetCalculatedEngineLoad(self):
        load = self.entCalculatedEngineLoad.get()
        self.device.setCalculatedEngineLoad(int(load, 10))

    def cmdTest(self):
        print "test"
        obd.main()
        
        

    def callback(self):
        print "Callback!"

    
    def createWidgets(self):
        self.paramControl(1, "EngineRPM",              self.cmdSetEngineRPM,            self.cmdDecreaseEngineRPM,       self.cmdIncreaseEngineRPM,       2, 1)
        self.paramControl(2, "Vehicle Speed",          self.cmdSetVehicleSpeed,         self.cmdSetVehicleSpeed,         self.cmdSetVehicleSpeed,         3, 1)        
        self.paramControl(3, "Throttle",               self.cmdSetThrottlePosition,     self.cmdDecreaseEngineRPM,       self.cmdIncreaseEngineRPM,       4, 1)
        self.paramControl(4, "Fuel Level Input",       self.cmdSetFuelLevelInput,       self.cmdDecreaseEngineRPM,       self.cmdIncreaseEngineRPM,       5, 1)
        self.paramControl(5, "Engine Fuel Rate",       self.cmdSetEngineFuelRate,       self.cmdSetEngineFuelRate,       self.cmdSetEngineFuelRate,       6, 1)
        self.paramControl(6, "MAF Air Flow Rate",      self.cmdSetMAFAirFlowRate,       self.cmdSetMAFAirFlowRate,       self.cmdSetMAFAirFlowRate,       7, 1)
        self.paramControl(7, "Calculated Engine Load", self.cmdSetCalculatedEngineLoad, self.cmdSetCalculatedEngineLoad, self.cmdSetCalculatedEngineLoad, 8, 1)
        
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

        '''self.lblEngineRPM = Label(self)
        self.lblEngineRPM["text"] = "Engine RPM"
        self.lblEngineRPM.grid(sticky="W", row=2, column=1)
        self.entEngineRPM = Entry(self, validate="focusout", validatecommand=self.cmdSetEngineRPM)
        self.entEngineRPM.grid(sticky="W", row=2, column=3)
        self.btnSetEngineRPM = Button(self)
        self.btnSetEngineRPM["text"] = "Apply"
        self.btnSetEngineRPM["command"] = self.cmdSetEngineRPM
        self.btnSetEngineRPM.grid(sticky="W", row=2, column=5)
        self.btnDecEngineRPM = Button(self)
        self.btnDecEngineRPM["text"] = "-"
        self.btnDecEngineRPM["command"] = self.cmdDecreaseEngineRPM
        self.btnDecEngineRPM.grid(sticky="W", row=2, column=2)
        self.btnIncEngineRPM = Button(self)
        self.btnIncEngineRPM["text"] = "+"
        self.btnIncEngineRPM["command"] = self.cmdIncreaseEngineRPM
        self.btnIncEngineRPM.grid(sticky="W", row=2, column=4)

        self.lblVehicleSpeed = Label(self)
        self.lblVehicleSpeed["text"] = "Vehicle Speed"
        self.lblVehicleSpeed.grid(sticky="W", row=3, column=1)
        self.entVehicleSpeed = Entry(self, validate="focusout", validatecommand=self.cmdSetVehicleSpeed)
        self.entVehicleSpeed.grid(sticky="W", row=3, column=3)
        self.btnVehicleSpeed = Button(self)
        self.btnVehicleSpeed["text"] = "Apply"
        self.btnVehicleSpeed["command"] = self.cmdSetVehicleSpeed
        self.btnVehicleSpeed.grid(sticky="W", row=3, column=5)
        self.btnVehicleSpeed = Button(self)
        self.btnVehicleSpeed["text"] = "-"
        self.btnVehicleSpeed["command"] = self.cmdDecreaseEngineRPM
        self.btnVehicleSpeed.grid(sticky="W", row=3, column=2)
        self.btnVehicleSpeed = Button(self)
        self.btnVehicleSpeed["text"] = "+"
        self.btnVehicleSpeed["command"] = self.cmdIncreaseEngineRPM
        self.btnVehicleSpeed.grid(sticky="W", row=3, column=4)

        self.lblThrottlePosition = Label(self)
        self.lblThrottlePosition["text"] = "Throttle Position"
        self.lblThrottlePosition.grid(sticky="W", row=4, column=1)
        self.entThrottlePosition = Entry(self, validate="focusout", validatecommand=self.cmdSetThrottlePosition)
        self.entThrottlePosition.grid(sticky="W", row=4, column=2)
        self.btnThrottlePosition = Button(self)
        self.btnThrottlePosition["text"] = "Apply"
        self.btnThrottlePosition["command"] = self.cmdSetThrottlePosition
        self.btnThrottlePosition.grid(sticky="W", row=4, column=3)

        #self.lblFuelLevelInput = Label(self)
        #self.lblFuelLevelInput["text"] = "Fuel Level Input"
        #self.lblFuelLevelInput.grid(sticky="W", row=5, column=1)
        self.entFuelLevelInput = Entry(self, validate="focusout", validatecommand=self.cmdSetFuelLevelInput)
        self.entFuelLevelInput.grid(sticky="W", row=5, column=2)
        self.btnFuelLevelInput = Button(self)
        self.btnFuelLevelInput["text"] = "Apply"
        self.btnFuelLevelInput["command"] = self.cmdSetFuelLevelInput
        self.btnFuelLevelInput.grid(sticky="W", row=5, column=3)
        

        self.lblEngineFuelRate = Label(self)
        self.lblEngineFuelRate["text"] = "Engine Fuel Rate"
        self.lblEngineFuelRate.grid(sticky="W", row=6, column=1)
        self.entEngineFuelRate = Entry(self, validate="focusout", validatecommand=self.cmdSetEngineFuelRate)
        self.entEngineFuelRate.grid(sticky="W", row=6, column=2)
        self.btnEngineFuelRate = Button(self)
        self.btnEngineFuelRate["text"] = "Apply"
        self.btnEngineFuelRate["command"] = self.cmdSetEngineFuelRate
        self.btnEngineFuelRate.grid(sticky="W", row=6, column=3)
        
        self.lblMAFAirFlowRate = Label(self)
        self.lblMAFAirFlowRate["text"] = "MAF Air Flow Rate"
        self.lblMAFAirFlowRate.grid(sticky="W", row=7, column=1)
        self.entMAFAirFlowRate = Entry(self, validate="focusout", validatecommand=self.cmdSetMAFAirFlowRate)
        self.entMAFAirFlowRate.grid(sticky="W", row=7, column=2)
        self.btnMAFAirFlowRate = Button(self)
        self.btnMAFAirFlowRate["text"] = "Apply"
        self.btnMAFAirFlowRate["command"] = self.cmdSetMAFAirFlowRate
        self.btnMAFAirFlowRate.grid(sticky="W", row=7, column=3)

        self.lblCalculatedEngineLoad = Label(self)
        self.lblCalculatedEngineLoad["text"] = "Calculated Engine Load"
        self.lblCalculatedEngineLoad.grid(sticky="W", row=8, column=1)
        self.entCalculatedEngineLoad = Entry(self, validate="focusout", validatecommand=self.cmdSetCalculatedEngineLoad)
        self.entCalculatedEngineLoad.grid(sticky="W", row=8, column=2)
        self.btnCalculatedEngineLoad = Button(self)
        self.btnCalculatedEngineLoad["text"] = "Apply"
        self.btnCalculatedEngineLoad["command"] = self.cmdSetCalculatedEngineLoad
        self.btnCalculatedEngineLoad.grid(sticky="W", row=8, column=3)

        #self.btnIncreaseEngineRPM = Button(self)
        #self.btnIncreaseEngineRPM["text"] = "Increase Engine RPM"
        #self.btnIncreaseEngineRPM["command"] = self.cmdIncreaseEngineRPM
        #self.btnIncreaseEngineRPM.pack({"side": "left"})

        #self.btnDecreaseEngineRPM = Button(self)
        #self.btnDecreaseEngineRPM["text"] = "Increase Engine RPM"
        #self.btnDecreaseEngineRPM["command"] = self.cmdDecreaseEngineRPM
        #self.btnDecreaseEngineRPM.pack({"side": "left"})'''



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.device = obd.OBDEmulator()
        self.pack()
        self.createWidgets()


root = Tk()
root.wm_title('OBD-II Emulator Control')
app = Application(master=root)
#root.configure(background='blue')
#app.configure(background='blue')
app.mainloop()
root.destroy()

