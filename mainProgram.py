#!/usr/bin/python

# interrupt-based GPIO example using LEDs and pushbuttons

import RPi.GPIO as GPIO
import time
import threading
import websocket

ws = websocket.WebSocket()
ws.connect("ws://localhost:1880/ws/example")
count = 0
ws.send("hideAll")
time.sleep(1)

GPIO.setmode(GPIO.BCM)

BTN_G = 2 # G17
coinVal=0.0
coinsChange=0
LED_G = 3 # G5
btn2led = {
	BTN_G: LED_G,

}

GPIO.setwarnings(False) # because I'm using the pins for other things too!
GPIO.setup([BTN_G], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup([LED_G], GPIO.OUT, initial=GPIO.HIGH)

# can't add separate callbacks for both rising and falling
#GPIO.add_event_detect(BTN_B, GPIO.RISING, lambda pin: GPIO.output(LED_B, False))
#GPIO.add_event_detect(BTN_B, GPIO.FALLING, lambda pin: GPIO.output(LED_B, True))


def handle(pin):
    global coinsChange
    global coinVal
	# light corresponding LED when pushbutton of same color is pressed
	GPIO.output(btn2led[pin], not GPIO.input(pin))

	t = None
	if pin == BTN_G:
		# when green and red pressed simultaneously, enter blink mode
		if GPIO.input(BTN_G):

            print("coin detected")
            coinVal=coinVal+0.05
            coinsChange=1

GPIO.add_event_detect(BTN_G, GPIO.RISING, handle)
ws.send("hideAll")
# TODO: pause?
while True:
    if(coinsChange==1):
        coinsChange=0
        print("coins="+coinVal)
        ws.send("cVal;"+coinVal)
	time.sleep(1.2)

