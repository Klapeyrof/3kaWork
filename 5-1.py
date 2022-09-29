import RPi.GPIO as GPIO
import time

dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

a=int()

def func(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

def adc():
    for i in range (256):
        signal=func(i)
        GPIO.output(dac,signal)
        compvalue=GPIO.input(comp)
        time.sleep(0.005)
        if(compvalue==0):
            return i



    
    GPIO.output(dac,signal)
    return signal

try:
    while True:
        k=adc()
        voltage= float(int(3.3*k/256*100)/100)
        print("ADC value= ",k," -> ",func(k),"voltage= ",voltage)
    

finally:
    GPIO.output(dac,1)
    GPIO.cleanup()