#!/usr/bin/python3
import os, signal, multiprocessing
import lib.env, lib.nics
import module.CPU.stream
import module.websocket

class IndexController():

  debug = 0
  isStereo = 0
  w, h = 800, 600

  def __init__(self):
    self.args = lib.env.init()
    self.debug = self.args.debug
    self.ws = module.websocket.Websocket()

    self.cameraQ1 = multiprocessing.Queue()

    # use env to change values. Example:
    # wsip=172.10.0 python3 index.py
    self.wsip = '192.168.1.' if os.getenv('wsip') == None else os.getenv('wsip')
    self.wspr = '5001' if os.getenv('wspr') == None else os.getenv('wspr')

  def indexAction(self):
    print("Index:Index. Selected processor: %s ".center(80, ".") % self.args.proc)

    streamer = module.CPU.stream.Stream()
    streamer.setFrameWH(self.w, self.h)
    source = streamer.getSource()

    if (len(source) == 0):
      raise Exception('Unable to identify active camera.')

    def asyncStream(cameraIx, q) -> None:
      streamer.startCamera(source[cameraIx], q)

    def asyncWebsocket(cameraIx, q)-> None:
      ip = None
      ips = lib.nics.getIPList()

      for val in ips:
        if val.startswith(self.wsip):
          ip = val

      ws = module.websocket.Websocket()
      ws.start(q, ip, self.wspr)

    p1 = multiprocessing.Process(target=asyncStream, args=(self.isStereo, self.cameraQ1, ))
    p2 = multiprocessing.Process(target=asyncWebsocket, args=[self.isStereo, self.cameraQ1, ])
    p1.start()
    p2.start()

    def asyncTerminate(signalReceived, frame) -> None:
      print('Terminate multiprocess. Received signal: %d'.center(80, '.') % signalReceived)
      if 'p1' in vars():
        p1.terminate()
        p1.join()
      if 'p2' in vars():
        p2.terminate()
        p2.join()

    signal.signal(signal.SIGINT, asyncTerminate)

