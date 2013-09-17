#!/usr/bin/env python

import pypm
import array
import time

class MidiListener:
    stop = False
    _chord=[]
    _updateList=[]

    def __init__(self):
        pypm.Initialize() # always call this first, or OS may crash when you try to open a stream
    def __del__(self):
        pypm.Terminate()
    
    def PrintInputDevices(self):
        for loop in range(pypm.CountDevices()):
            interf,name,inp,outp,opened = pypm.GetDeviceInfo(loop)
            if (inp == 1):
                print loop, name," ",
                if (opened == 1): print "(opened)"
                else: print "(unopened)"
        print
        
    def Listen(self):
        print self._updateList
        self.PrintInputDevices()
        dev = int(raw_input("Type input number: "))
        MidiIn = pypm.Input(dev)
        print "Midi Input opened. Reading Midi messages..."
    #    MidiIn.SetFilter(pypm.FILT_ACTIVE | pypm.FILT_CLOCK)
        while self.stop != True: # never stop reading midi messages, unless someone says so
            while not MidiIn.Poll(): pass
            MidiData = MidiIn.Read(1) # read only 1 message at a time
            signal = MidiData[0][0][0]
            value = MidiData[0][0][1]
            if signal!=144 & signal!=128:
                continue
            if signal==144:
                try:
                    self._chord.remove(value)
                except:
                    self._chord.append(value)
            if signal==128:
                self._chord.remove(value)
            self.Update()
            #print "Got message at time ",MidiData[0][1],", ",
            #print  MidiData[0][0][0]," ",MidiData[0][0][1]," ",MidiData[0][0][2], MidiData[0][0][3]
            # NOTE: most Midi messages are 1-3 bytes, but the 4 byte is returned for use with SysEx messages.
        del MidiIn

    def GetChord(self):
        return self._chord

    def AddUpdate(self,function):
        self._updateList.append(function)
    
    def RemoveUpdate(self,function):
        self._update.remove(function)

    def Update(self):
        for function in self._updateList:
            function()

    def Stop(self):
        self.stop = True
