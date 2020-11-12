#!/usr/bin/python3
import cv2, time
import lib.camera

class Stream():

  def __init__(self):
    print('CPU camera'.center(80, "~"))
    self.source = lib.camera.getSource()
    self.w, self.h = 800, 600

    print('Available video source: ', self.source)

  def setFrameWH(self, w, h):
    if (int(w)): self.w = int(w)
    if (int(h)): self.h = int(h)

  def getSource(self):
    return self.source

  def startCamera(self, sourceIx, q):
    cam = cv2.VideoCapture(sourceIx)
    cam.set(3, self.w)
    cam.set(4, self.h)

    print('Started camera %d '.center(80, "~") % sourceIx)

    while True:

      time.sleep(0.1)

      if not cam.grab():
        print("No more frames")
        break

      isRetrieved, frame = cam.read()

      # fill que with frames
      # keep up to 5 frames in que to prevent memory build up, but enougth to identify movements
      if isRetrieved == True and q.qsize() <= 5:
        q.put(frame)

      if cv2.waitKey(1) & 0xFF == ord('q'):
        break


