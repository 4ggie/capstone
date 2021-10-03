from machine import Pin
from time import sleep
import machine
import utime
import _thread

internal_led = machine.Pin(25, machine.Pin.OUT)

led = Pin(16, Pin.OUT)
Sensor = Pin(15,Pin.IN)

def second_thread():
    while True:
        print("second thread")
        internal_led.on()
        utime.sleep(0.1)
        internal_led.off()
        utime.sleep(0.1)

_thread.start_new_thread(second_thread, ())

while True:
        print("first thread")
        if Sensor.value() == 0:
            print("on")
            led.on()
            sleep(0.1)
        else:
            print("off")
            led.off()
            sleep(0.1)
            utime.sleep(0.3)

            
                
        
    
        