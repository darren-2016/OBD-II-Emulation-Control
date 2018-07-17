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

    def cmdTest(self):
        print "test"
        obd.main()
        
        

    def createWidgets(self):
        self.btnQuit = Button(self)
        self.btnQuit["text"] = "QUIT"
        self.btnQuit["fg"]   = "red"
        self.btnQuit["command"] =  self.quit

        self.btnQuit.pack({"side": "left"})

        self.btnConnectDevice = Button(self)
        self.btnConnectDevice["text"] = "Connect Device"
        self.btnConnectDevice["command"] = self.connectDevice
        self.btnConnectDevice.pack({"side": "left"})

        self.btnClose = Button(self)
        self.btnClose["text"] = "Close"
        self.btnClose["fg"]   = "red"
        self.btnClose["command"] =  self.closeDevice
        self.btnClose.pack({"side": "left"})


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.device = obd.OBDEmulator()
        self.pack()
        self.createWidgets()


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

