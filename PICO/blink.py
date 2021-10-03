from machine import Pin
from time import sleep
 
led = Pin(16, Pin.OUT)
 
for i in range(30):
    led.toggle()
    sleep(0.3)