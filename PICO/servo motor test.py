from machine import Pin, PWM
import utime

MID = 1500000
MIN = 1000000
MAX = 2000000

led = Pin(25,Pin.OUT)
pwm = PWM(Pin(15))
pwm2 = PWM(Pin(14))
pwm3 = PWM(Pin(13))

pwm.freq(50)
pwm.duty_ns(MID)
pwm2.freq(50)
pwm2.duty_ns(MID)
pwm3.freq(50)
pwm3.duty_ns(MID)


while True:
    pwm.duty_ns(MIN)
    pwm2.duty_ns(MIN)
    pwm3.duty_ns(MIN)
    utime.sleep(1)
    
    pwm.duty_ns(MID)
    pwm2.duty_ns(MID)
    pwm3.duty_ns(MID)
    utime.sleep(1)
    
    pwm.duty_ns(MAX)
    pwm2.duty_ns(MAX)
    pwm3.duty_ns(MAX)
    utime.sleep(1)
