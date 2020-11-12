#!/usr/bin/python3
import socket
import netifaces

def getIPList():

  ip = []

  for nic in netifaces.interfaces():
    addrs = netifaces.ifaddresses(nic)
    if netifaces.AF_INET in addrs:
      ip.append(addrs[netifaces.AF_INET][0]['addr'])

  return ip
