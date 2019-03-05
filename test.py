import time

import websocket

ws = websocket.WebSocket()
ws.connect("ws://localhost:1880/ws/example")
count = 0
ws.send("hideAll")
time.sleep(2)
while(count < 1):
    print( "Sending 'Hello, World'...")
    ws.send("cVal;22")
    print ("Sent")
    time.sleep(5)
    count = count + 1

ws.close()