# GUI.py
import Tkinter
from Tkinter import *
import obd

window=Tk()

print "GUI"

class Application(Frame):
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
        self.device.setEngineRPM(int(rpm))

    def cmdTest(self):
        print "test"
        obd.main()
        
        

    def callback(self):
        print "Callback!"

    def createWidgets(self):
        self.btnQuit = Button(self)
        self.btnQuit["text"] = "QUIT"
        self.btnQuit["fg"]   = "red"
        self.btnQuit["command"] =  self.quit
        #self.btnQuit.pack({"side": "left"})
        self.btnQuit.grid(row=6,column=1)

        self.btnConnectDevice = Button(self)
        self.btnConnectDevice["text"] = "Connect Device"
        self.btnConnectDevice["command"] = self.connectDevice
        #self.btnConnectDevice.pack({"side": "left"})
        self.btnConnectDevice.grid(row=1, column=1)

        self.btnClose = Button(self)
        self.btnClose["text"] = "Close"
        self.btnClose["fg"]   = "red"
        self.btnClose["command"] =  self.closeDevice
        #self.btnClose.pack({"side": "left"})
        self.btnClose.grid(row=1, column=2)

        self.lblEngineRPM = Label(self)
        self.lblEngineRPM["text"] = "Engine RPM"
        #self.lblEngineRPM.pack({"side": "left"})
        self.lblEngineRPM.grid(row=2, column=1)

        self.entEngineRPM = Entry(self, validate="focusout", validatecommand=self.cmdSetEngineRPM)
        #self.entEngineRPM.pack({"side": "left"})
        self.entEngineRPM.grid(row=2, column=2)

        self.btnSetEngineRPM = Button(self)
        self.btnSetEngineRPM["text"] = "Apply"
        self.btnSetEngineRPM["command"] = self.cmdSetEngineRPM
        #self.btnSetEngineRPM.pack({"side": "left"})
        self.btnSetEngineRPM.grid(row=2, column=3)

        self.lblVehicleSpeed = Label(self)
        self.lblVehicleSpeed["text"] = "Vehicle Speed"
        #self.lblVehicleSpeed.pack({"side": "bottom"})
        self.lblVehicleSpeed.grid(row=3, column=1)


        self.lblEngineFuelRate = Label(self)
        self.lblEngineFuelRate["text"] = "Engine Fuel Rate"
        self.lblEngineFuelRate.grid(row=4, column=1)
        

        #self.btnIncreaseEngineRPM = Button(self)
        #self.btnIncreaseEngineRPM["text"] = "Increase Engine RPM"
        #self.btnIncreaseEngineRPM["command"] = self.cmdIncreaseEngineRPM
        #self.btnIncreaseEngineRPM.pack({"side": "left"})

        #self.btnDecreaseEngineRPM = Button(self)
        #self.btnDecreaseEngineRPM["text"] = "Increase Engine RPM"
        #self.btnDecreaseEngineRPM["command"] = self.cmdDecreaseEngineRPM
        #self.btnDecreaseEngineRPM.pack({"side": "left"})



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.device = obd.OBDEmulator()
        self.pack()
        self.createWidgets()


root = Tk()
root.wm_title('OBD-II Emulator Control')
app = Application(master=root)
app.mainloop()
root.destroy()

