#!/usr/bin/env python3
import asyncio, websockets, cv2
import base64

class Websocket():

  def __init__(self):
    print('Start websocket server'.center(80, '~'))
    self.users = []

  def start(self, q, ip, port):
      users = self.users

      async def send(img):
        for user in users:
          try:
            await user.send(img)
          except:
            i = users.index(user)
            users.pop(i)

      async def time(websocket, path):
        users.append(websocket)
        while True:
          try:
            if websocket in users and users.index(websocket) > 0:
              await asyncio.sleep(1)
            else:
              if q.qsize() > 1:
                while q.qsize() > 4: q.get()
                encoded, buffer = cv2.imencode('.jpg', q.get())
                await send(base64.b64encode(buffer))
          except:
            print('error')

          await asyncio.sleep(0.1)

      print("starting WebSocket stream on %s:%s".center(80, '~') % (ip, port))
      start_server = websockets.serve(time, ip, port)
      asyncio.get_event_loop().run_until_complete(start_server)
      asyncio.get_event_loop().run_forever()






