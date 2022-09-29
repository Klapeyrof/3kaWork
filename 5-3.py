import RPi.GPIO as GPIO
import time

dac = [26,19,13,6,5,11,9,10]
leds=[21,20,16,12,7,8,25,24]
comp = 4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)
GPIO.setup(leds,GPIO.OUT)
GPIO.output(leds,0)
GPIO.setup(troyka,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(comp,GPIO.IN)

a=int()

def func(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

def adc():
    signal1=128
    signal2=64
    answer=0
    for i in range (8):
        signal=func(int(answer))
        GPIO.output(dac,signal)
        time.sleep(0.01)
        compvalue=GPIO.input(comp)
        if(compvalue==0):
            if(answer!=0):
                answer-=signal1
        else:
            answer += signal1
        signal1/=2
        signal2/=2
    lst=func(int(answer))
    voltage= float(int(3.3*answer/256*100)/100)
    x=voltage/3.3*8
    GPIO.output(leds[i],0)
    for i in range (8):
        if i<x:
            GPIO.output(leds[i],1)
        else:
            GPIO.output(leds[i],0)
    return int(answer)

print(adc())



try:
    while True:
        k=adc()
        voltage= float(int(3.3*k/256*100)/100)
        print("ADC value= ",k," -> ",func(k),"voltage= ",voltage)
    

finally:
    GPIO.output(dac,1)
    GPIO.cleanup()