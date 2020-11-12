#!/usr/bin/python3
import os
import cv2

def getSource(cams_test = 3):
  source = []

  for i in range(0, cams_test):
    try:
      cap = cv2.VideoCapture(i)
      test, frame = cap.read()
      if test:
        source.append(i)
    except:
      print('failed ')

  """
  devs = os.listdir('/dev/video*')

  print(devs)

  source = [int(dev[-1]) for dev in devs if dev.startswith('video')]
  source = sorted(source)

  print('looking for source')
  """
  return source
