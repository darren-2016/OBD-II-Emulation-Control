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


def main():
  obd = OBDEmulator()

  print 'OBD-II Emulator Controller'
  
  obd.connectDevice()

  #obd.sendCmd("ATZ")

  obd.sendCommand("ATVIN0")

  obd.sendCommand("ATSET 010C=1800")

 
if __name__ == "__main__":
    main()
