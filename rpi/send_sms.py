#!/usr/bin/env python
# -*- coding: utf-8 -*-
import serial
import os, time

class SendSMS():
    def __init__(self):
        self.initGPRS()

    def initGPRS(self):
        # Enable Serial Communication
        port = serial.Serial(port='/dev/ttyAMA0', baudrate=115200, timeout=1)
        self.port = port

        print "\n Sync baud: \n"
        for i in range(3):
          #sync baud rate
          port.write('AT'+'\r\n')
          rcv = port.read(100)
          time.sleep(1)
          print "."

        # Transmitting AT Commands to the Modem
        # '\r\n' indicates the Enter key
        port.write('AT+CMEE=1'+'\r\n')  # Select Message format as Text mode
        rcv = port.read(100)
        print 'Extend error message: %s' % rcv
        time.sleep(2)

        port.write('ATE0'+'\r\n')      # Disable the Echo
        rcv = port.read(100)
        time.sleep(2)

        port.write('AT+CMGF=1'+'\r\n')  # Select Message format as Text mode
        rcv = port.read(100)
        print 'Msg text format: %s' % rcv
        time.sleep(2)

        port.write('AT+CSCS="GSM"'+'\r\n')  # Select Message format as Text mode
        rcv = port.read(100)
        print 'GSM mode: %s' % rcv
        time.sleep(2)

        port.write('AT+CNMI=2,1,0,0,0'+'\r\n')   # New SMS Message Indications
        rcv = port.read(100)
        print 'New message indication: %s' % rcv
        time.sleep(1)

    def getIMEI(self):

        self.port.write('AT+GSN'+'\r\n')
        IMEI = self.port.read(100)
        IMEI = IMEI.replace('OK', '').strip()
        time.sleep(1)
        return IMEI

    def getSIMID(self):
        self.port.write('AT+CCID'+'\r\n')
        SIMID = self.port.read(100)
        time.sleep(1)
        return SIMID.replace('OK', '').strip()

    def receiveSMS(self):
      self.port.write('AT+CMGL="ALL"'+'\r\n')
      rsp = self.port.read(10000)
#      print "All SMS: \n %s" % rsp
      time.sleep(1)
      return rsp

    def deleteSMS(self):
      self.port.write('AT+CMGDA="DEL ALL"'+'\r\n')
      rsp = self.port.read(100)
      print 'Delete all SMS: %s' % rsp
      time.sleep(1)


    def sendText(self, mob, msg):
        port = self.port

        # Sending a message to a particular Number
        #print "Set phone"
        port.write('AT+CMGS="' + mob +  '"'+'\r\n')
        rcv = port.read(100)
        print rcv
        time.sleep(1)

        port.write(msg + '\r\n')  # Message
        isSetMsg = port.read(100)
        print 'Set msg: %s' % isSetMsg

        print "Sending ... "
        port.write("\x1A") # Enable to send SMS

        for i in range(10):
            isDelivered = port.read(100)
            print isDelivered

            if (isDelivered):
              return {'isDelivered': isDelivered}

