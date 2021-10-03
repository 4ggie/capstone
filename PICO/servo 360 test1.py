from machine import Pin, PWM
from utime import sleep

servo = PWM(Pin(14))

servo.freq(50)

while True:
    servo.duty_u16(1310)#ccw
    sleep(2)
    servo.duty_u16(4900)#stop
    sleep(2)
    servo.duty_u16(8200)#cw
    sleep(2)
