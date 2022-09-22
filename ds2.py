import RPi.GPIO as GPIO
import time
dac=[26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
a=int()
def func(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

try:
    while True:
        T=float(input())
        t=(T/256)/2
        for j in range(256):
            GPIO.output(dac,func(j))
            time.sleep(t)
        for j in range(255,-1,-1):
            GPIO.output(dac,func(j))
            time.sleep(t)

finally:
    GPIO.output(dac,1)
    GPIO.cleanup()    



