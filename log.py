############################################################
# OBD-II Emulator Control Application
# 
# Module: log.py
#

global LOGLEVEL

LOGLEVEL = 0

#class logging:
def output(logstring):
    global LOGLEVEL
    if LOGLEVEL == 1:
        print (logstring)

def level(loglevel):
    global LOGLEVEL
    if loglevel == 1:
        LOGLEVEL = 1
    else:
        LOGLEVEL = 0

def readloglevel():
    global LOGLEVEL
    return LOGLEVEL

