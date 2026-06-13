from machine import Pin
import time

PINS = [2, 5, 15, 4]
leds = [Pin(p, Pin.OUT) for p in PINS]

def all_off():
    for led in leds:
        led.off()

while True:
    
    steps = [0, 1, 2, 3, 2, 1]
    
    for s in steps:
        all_off()          
        leds[s].on()       
        time.sleep(0.5)    
