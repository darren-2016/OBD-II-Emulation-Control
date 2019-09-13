################################################################################
# OBD-II Emulator Control Application
#
# Python-based controller application for the Freematics OBD-II Emulator
#
# Module: obd.py

import serial
import serial.tools.list_ports
import log

########################################
# OBDEmulator class
#
class OBDEmulator:
  baudRate = 38400
  portIdString = "10C4:EA60"

  def __init__(self, verbose=True):
    self.verbose = verbose

  ########################################
  # scanSerialPorts
  def scanSerialPorts(self, guiObject):
    log.output ("Scanning serial ports")
    portlist = serial.tools.list_ports
    
    iterator = serial.tools.list_ports.grep(self.portIdString)
    
    #for i in portlist:
    #  log.output (i.ListPortInfo)
    
    devicesFound = 0
    
    for c, (port, desc, hwid) in enumerate(iterator):
      devicesFound = devicesFound + 1
      portPath = format(port)
    '''
    port = '/dev/tty.SLAB_USBtoUART'
    portPath = format(port)
    devicesFound = 1
    '''
    
    if devicesFound == 1:
      log.output("Found OBD-II device {}".format(portPath))
      return True, portPath
    else:
      log.output("{} OBD-II devices found".format(devicesFound))
      return False, ""

  ########################################
  # connectDevice
  def connectDevice(self, guiObject):
    i, portPath = self.scanSerialPorts(guiObject)
    #i = True
    #portPath = '/dev/tty.SLAB_USBtoUART'
    
    if i == True:
      log.output ("Connecting")
      guiObject.writeLogText("Connecting\n")
      self.serialPort = serial.Serial(portPath, baudrate=self.baudRate, timeout=1)
      log.output ("Connected to: " + self.serialPort.name)
      return True
    else:
      return False

    

  ########################################
  # closeConnection
  def closeConnection(self, guiObject):
    log.output ("Disconnecting")
    guiObject.writeLogText("Disconnecting\n")
    self.serialPort.close()

  ########################################
  # sendCommand
  def sendCommand(self, guiObject, command):
    self.serialPort.write((command.encode() + b'\r'))
    guiObject.writeLogText('>>' + command + '\r')
    out = self.serialPort.readline()
    log.output ('<<' + out.decode())
    guiObject.writeLogText(out.decode())
    #out = self.serialPort.readline()
    #log.output ('<<' + out)
    #out = self.serialPort.readline()
    #log.output ('<<' + out)
    #out = self.serialPort.readline()
    #log.output ('<<' + out)
    #out = self.serialPort.readline()
    #log.output ('<<' + out)
    #out = self.serialPort.readline()
    #log.output ('<<' + out)

  ########################################
  # Function:    setPidValue
  # Parameters:  pid (string), pidValue (integer)
  # Description: Set PID Value
  def setPIDValue(self, guiObject, pid, pidValue):
    self.sendCommand(guiObject, "ATSET " + pid + "=" + str(pidValue))
    log.output ("PID = " + pid)
    log.output ("PID Value = " + str(pidValue))

  
  ########################################
  # Function:    setEngineRPM
  # Parameters:  rpm (rpm)
  # Description: PID=010C
  def setEngineRPM(self, guiObject, rpm):
      self.sendCommand(guiObject, "ATSET 010C=" + str(rpm))

  ########################################
  # Function:    setVehicleSpeed
  # Parameters:  speed (km/h)
  # Description: PID=010D
  def setVehicleSpeed(self, guiObject, speed):
    self.sendCommand(guiObject, "ATSET 010D=" + str(speed))

  ########################################
  # Function:    setThrottlePosition
  # Parameters:  throttle (0 - 100%)
  # Description: PID=0111
  def setThrottlePosition(self, guiObject, throttle):
    self.sendCommand(guiObject, "ATSET 0111=" + str(throttle))
  
  ########################################
  # Function:    setFuelLevelInput
  # Parameters:  fuelLevel (0 - 100%)
  # Description: PID=012F
  def setFuelLevelInput(self, guiObject, fuelLevel):
    self.sendCommand(guiObject, "ATSET 012F=" + str(fuelLevel))
  
  ########################################
  # Function:    setEngineFuelRate
  # Parameters:  rate (L/h)
  # Description: PID=015E
  def setEngineFuelRate(self, guiObject, rate):
    self.sendCommand(guiObject, "ATSET 015E=" + str(rate))
  
  def getEngineFuelRate(self, guiObject):
    self.sendCommand(guiObject, "ATGET 015E")
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    out = self.serialPort.readline()
    log.output ("<<<<< " + str(out))
    
  ########################################
  # Function:    setMAFAirFlowRate
  # Parameters:  rate (g/s)
  # Description: PID=0110
  def setMAFAirFlowRate(self, guiObject, rate):
    self.sendCommand(guiObject, "ATSET 0110=" + str(rate))

  ########################################
  # Function:    setCalculatedEngineLoad
  # Parameters:  rate (%)
  # Description: PID=0104
  def setCalculatedEngineLoad(self, guiObject, load):
    self.sendCommand(guiObject, "ATSET 0104=" + str(load))


########################################
# Function:     main
# Description:  Main function.
def main():
  obd = OBDEmulator()

  log.output ('OBD-II Emulator Controller')
  
  obd.connectDevice()

  #obd.sendCmd("ATZ")

  #obd.sendCommand("ATVIN0")

  #obd.setEngineRPM(1600)
  #obd.setVehicleSpeed(50)
  #obd.setThrottlePosition(19)
  #obd.setFuelLevelInput(66)
  #obd.setEngineFuelRate(111)
  #obd.getEngineFuelRate()
  #obd.setMAFAirFlowRate(99)
  #obd.setCalculatedEngineLoad(48)

  #obd.sendCommand("ATSET 010C=1800")

 
if __name__ == "__main__":
    main()
