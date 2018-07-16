################################################################################
# OBD-II Emulator Controller
# Python-based controller application for the Freematics OBD-II Emulator
#

import serial
import serial.tools.list_ports


####################
# OBDEmulator class
#
class OBDEmulator:
  baudRate = 38400
  portIdString = "10C4:EA60"

  def __init__(self, verbose=True):
    self.verbose = verbose

  ####################
  # scanSerialPorts
  def scanSerialPorts(self):
    #portlist = serial.tools.list_ports
    iterator = serial.tools.list_ports.grep(self.portIdString)

    devicesFound = 0
    for c, (port, desc, hwid) in enumerate(iterator):
      devicesFound = devicesFound + 1
      portPath = format(port)

    if devicesFound == 1:
      print("Found OBD-II device {}".format(portPath))
      return True, portPath
    else:
      print("{} OBD-II devices found".format(devicesFound))
      return False

  ####################
  # connectDevice
  def connectDevice(self):
    i, portPath = self.scanSerialPorts()
    if i == True:
      print "Connecting"
      self.serialPort = serial.Serial(portPath, baudrate=self.baudRate, timeout=1)

  ####################
  # closeConnection
  def closeConnection(self):
    self.serialPort.close()

  ####################
  # sendCommand
  def sendCommand(self, command):
    self.serialPort.write((command + '\r'))
    out = self.serialPort.readline()
    print '<<' + out
    out = self.serialPort.readline()
    print '<<' + out
    out = self.serialPort.readline()
    print '<<' + out
    out = self.serialPort.readline()
    print '<<' + out
    out = self.serialPort.readline()
    print '<<' + out
    out = self.serialPort.readline()
    print '<<' + out

  ##############################
  # setEngineRPM
  # PID: 010C
  # rpm : rpm
  def setEngineRPM(self, rpm):
      self.sendCommand("ATSET 010C=" + str(rpm))

  ##############################
  # setVehicleSpeed
  # PID: 010D
  # speed : km/h
  def setVehicleSpeed(self, speed):
    self.sendCommand("ATSET 010D=" + str(speed))

  ##############################
  # setThrottlePosition
  # PID: 0111
  # throttle : 0 - 100%
  def setThrottlePosition(self, throttle):
    self.sendCommand("ATSET 0111=" + str(throttle))
  
  ##############################
  # setFuelLevelInput
  # PID: 012F
  # fuelLevel : 0 - 100%
  def setFuelLevelInput(self, fuelLevel):
    self.sendCommand("ATSET 012F=" + str(fuelLevel))
  
  ##############################
  # setEngineFuelRate
  # PID: 015E
  # rate: L/h
  def setEngineFuelRate(self, rate):
    self.sendCommand("ATSET 015E=" + str(rate))
  
  ##############################
  # setMAFAirFlowRate
  # PID: 0110
  # rate : g/s
  def setMAFAirFlowRate(self, rate):
    self.sendCommand("ATSET 0110=" + str(rate))

  ##############################
  # setCalculatedEngineLoad
  # PID: 0104
  # rate : %
  def setCalculatedEngineLoad(self, load):
    self.sendCommand("ATSET 0104=" + str(load))


def main():
  obd = OBDEmulator()

  print 'OBD-II Emulator Controller'
  
  obd.connectDevice()

  #obd.sendCmd("ATZ")

  obd.sendCommand("ATVIN0")

  obd.setEngineRPM(1600)
  obd.setVehicleSpeed(50)
  obd.setThrottlePosition(19)
  obd.setFuelLevelInput(66)
  obd.setEngineFuelRate(111)
  obd.setMAFAirFlowRate(99)
  obd.setCalculatedEngineLoad(48)

  #obd.sendCommand("ATSET 010C=1800")

 
if __name__ == "__main__":
    main()
