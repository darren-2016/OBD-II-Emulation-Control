############################################################
# OBD-II Emulator Control Application
# 
# Module: GUI.py
#

import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import obd
import log

#window=Tk()



log.output("GUI")

bgcolour = 'lightblue'
title = 'OBD-II Emulator Control'

        

class Application(ttk.Frame):
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
        log.output ("Label = " + label)
        self.label = label
        self.callback = callback

        # Parameter Label
        self.lbl[index] = ttk.Label(self)
        self.lbl[index]["text"] = self.label
        self.lbl[index].grid(sticky="W", row=row, column=column)
        #self.lbl[index].configure(background=bgcolour)

        # Parameter Decrement Button
        self.btnDec[index] = ttk.Button(self)
        self.btnDec[index]["text"] = "-"
        self.btnDec[index]["command"] = callbackDecParameter
        self.btnDec[index].grid(sticky="E", row=row, column=column+2)
        #self.btnDec[index].configure(highlightbackground=bgcolour)

        # Parameter Entry
        self.ent[index] = ttk.Entry(self, validate="focusout", validatecommand=callback)
        self.ent[index].grid(sticky="NSWE", row=row, column=column+3, columnspan=2)
        #self.ent[index].configure(highlightbackground=bgcolour)
        
        # Parameter Increment Button
        self.btnInc[index] = ttk.Button(self)
        self.btnInc[index]["text"] = "+"
        self.btnInc[index]["command"] = callbackIncParameter
        self.btnInc[index].grid(sticky="W", row=row, column=column+5)
        #self.btnInc[index].configure(highlightbackground=bgcolour)

        # Parameter Setting Apply Button
        self.btnSet[index] = ttk.Button(self)
        self.btnSet[index]["text"] = "Apply"
        self.btnSet[index]["command"] = callback
        self.btnSet[index].grid(sticky="W", row=row, column=column+6)
        #self.btnSet[index].configure(highlightbackground=bgcolour)



    def initialiseParams(self):
        for i in range(self.ID_ENGINERPM, self.ID_CALCULATEDENGINELOAD + 1):
            self.ent[i].insert(0, self.paramValue[i])
        log.output("")


    def connectDevice(self):
        self.device.connectDevice()
        self.lblStatus["text"] = "Status: Connected"
        self.btnConnectDevice["state"] = "disabled"
        self.btnDisconnect["state"] = "normal"
    
    def closeDevice(self):
        self.device.closeConnection()
        self.lblStatus["text"] = "Status: Disconnected"
        self.btnConnectDevice["state"] = "normal"
        self.btnDisconnect["state"] = "disabled"


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

    def cmdIncByPID(self):
        self.cmdSetByPID(self.INC)

    def cmdDecByPID(self):
        self.cmdSetByPID(self.DEC)

    def cmdSetByPID(self, mode=SET):
        pid = self.entPID.get()
        pidValue = int(self.entPIDValue.get(), base=10)
        if mode == self.INC:
            pidValue = pidValue + 1
            self.entPIDValue.delete(0, END)
            self.entPIDValue.insert(0, pidValue)
        if mode == self.DEC:
            pidValue = pidValue - 1
            self.entPIDValue.delete(0, END)
            self.entPIDValue.insert(0, pidValue)

        self.device.setPIDValue(pid, pidValue)
    
        ###pid = self.entPID.get()
        ###pidValue = self.entPIDValue.get()
        log.output ("PID = " + pid)
        log.output ("PID Value= " + str(pidValue))


    def cmdTest(self):
        log.output ("test")
        obd.main()
        

    def callback(self):
        log.output ("Callback!")

    
    def createWidgets(self):
        self.paramControl(self.ID_ENGINERPM,            "EngineRPM",              self.cmdSetEngineRPM,            self.cmdDecreaseEngineRPM,            self.cmdIncreaseEngineRPM,             4, 1)
        self.paramControl(self.ID_VEHICLESPEED,         "Vehicle Speed",          self.cmdSetVehicleSpeed,         self.cmdDecreaseVehicleSpeed,         self.cmdIncreaseVehicleSpeed,          5, 1)        
        self.paramControl(self.ID_THROTTLEPOSITION,     "Throttle",               self.cmdSetThrottlePosition,     self.cmdDecreaseThrottlePosition,     self.cmdIncreaseThrottlePosition,      6, 1)
        self.paramControl(self.ID_FUELLEVELINPUT,       "Fuel Level Input",       self.cmdSetFuelLevelInput,       self.cmdDecreaseFuelLevelInput,       self.cmdIncreaseFuelLevelInput,        7, 1)
        self.paramControl(self.ID_ENGINEFUELRATE,       "Engine Fuel Rate",       self.cmdSetEngineFuelRate,       self.cmdDecreaseEngineFuelRate,       self.cmdIncreaseEngineFuelRate,        8, 1)
        self.paramControl(self.ID_MAFAIRFLOWRATE,       "MAF Air Flow Rate",      self.cmdSetMAFAirFlowRate,       self.cmdDecreaseMAFAirFlowRate,       self.cmdIncreaseMAFAirFlowRate,        9, 1)
        self.paramControl(self.ID_CALCULATEDENGINELOAD, "Calculated Engine Load", self.cmdSetCalculatedEngineLoad, self.cmdDecreaseCalculatedEngineLoad, self.cmdIncreaseCalculatedEngineLoad, 10, 1)
        
        self.lblVIN = ttk.Label(self)
        self.lblVIN["text"] = "VIN"
        self.lblVIN.grid(sticky="W", row=3, column=1)

        self.entVIN = ttk.Entry(self) #, validate="focusout", validatecommand=cmdVIN)
        self.entVIN.grid(sticky="NSWE", row=3, column=2, columnspan=4)

        self.btnVIN = ttk.Button(self)
        self.btnVIN["text"] = "Apply"
        self.btnVIN.grid(row=3,column=7)        

        self.btnQuit = ttk.Button(self)
        self.btnQuit["text"] = "QUIT"
        self.btnQuit["command"] =  ask_quit
        self.btnQuit.grid(row=1,column=5)

        self.btnConnectDevice = ttk.Button(self)
        self.btnConnectDevice["text"] = "Connect Device"
        self.btnConnectDevice["command"] = self.connectDevice
        self.btnConnectDevice.grid(row=1, column=1)

        self.btnDisconnect = ttk.Button(self)
        self.btnDisconnect["text"] = "Disconnect Device"
        self.btnDisconnect["command"] =  self.closeDevice
        self.btnDisconnect.grid(row=1, column=2)

        self.lblStatus = ttk.Label(self)
        self.lblStatus["text"] = "Status: Disconnected"
        self.lblStatus.grid(sticky="W", row=2, column=1)

        self.lblPID = ttk.Label(self)
        self.lblPID["text"] = "PID"
        self.lblPID.grid(sticky="W", row=11, column=1)

        self.entPID = ttk.Entry(self)
        self.entPID.grid(sticky="NSWE", row=11, column=2)

        self.btnPIDValueDec = ttk.Button(self)
        self.btnPIDValueDec["text"] = "-"
        self.btnPIDValueDec["command"] = self.cmdDecByPID
        self.btnPIDValueDec.grid(sticky="E", row=11,column=3)

        self.entPIDValue = ttk.Entry(self)
        self.entPIDValue.grid(sticky="NSWE", row=11, column=4, columnspan=2)

        self.btnPIDValueInc = ttk.Button(self)
        self.btnPIDValueInc["text"] = "+"
        self.btnPIDValueInc["command"] = self.cmdIncByPID
        self.btnPIDValueInc.grid(sticky="W", row=11,column=6)

        self.btnPIDValueApply = ttk.Button(self)
        self.btnPIDValueApply["text"] = "Apply"
        self.btnPIDValueApply["command"] = self.cmdSetByPID
        self.btnPIDValueApply.grid(row=11,column=7)
        


    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)
        self.device = obd.OBDEmulator()
        self.pack()
        self.createWidgets()
        self.initialiseParams()



############################################################
# Quit confirmation popup dialog
#
def ask_quit():
    if messagebox.askokcancel("Quit", "You want to quit now?"):
        root.destroy()

############################################################
# About popup dialog
#
def popup_about():
    win = Toplevel()
    win.wm_title("About...")
    win.columnconfigure(0, weight=1)
    win.rowconfigure(0, weight=1)

    frmAbout = ttk.Frame(win)
    frmAbout.grid(row=0, column=0, columnspan=1, sticky=N+S+E+W)
    frmAbout.grid_columnconfigure(0, weight=1)
    frmAbout.grid_rowconfigure(0, weight=1)

    
    l = ttk.Label(frmAbout, text=title, anchor=CENTER)
    l.grid(row=0, column=0, columnspan=1, sticky=N+S+E+W)

    l = ttk.Label(frmAbout, text="Version 0.0.1", anchor=CENTER)
    l.grid(row=1, column=0, columnspan=1, sticky=N+S+E+W)

    b = ttk.Button(frmAbout, text="OK", command=win.destroy)
    b.grid(row=2, column=0, columnspan=1, sticky=N+S+E+W)



root = Tk()

s = ttk.Style()
root.style = ttk.Style()
#log.output (s.theme_names())
root.style.theme_use('clam')
#root.style.theme_use('clam')
#root.style.configure('TButton', background='grey')
#root.style.configure('TButton', foreground='black')
#root.style.configure('TButton', highlightcolor='red')
root.style.map('TButton', background=[('disabled','#d9d9d9'), ('active','#ececec')], foreground=[('disabled','#a3a3a3')], relief=[('pressed', '!disabled', 'sunken')])
root.style.configure('TLabel', background='grey')
root.style.configure('TFrame', background='grey')




appVersion = "0.0.1"
root.wm_title(title + ' ' + appVersion)
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
#self.menubar.add_command(label="Hello!", command=hello)
filemenu.add_command(label="About", command=popup_about)
filemenu.add_command(label="Quit!", command=ask_quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)
root.configure(background=bgcolour)


root.protocol("WM_DELETE_WINDOW", ask_quit)
app = Application(master=root)

root.mainloop()



