import RPi.GPIO as GPIO
dac=[26,19,13,6,5,11,9,10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac,GPIO.OUT)

a=int()
def func(a):
    return[int(i) for i in bin(a)[2:].zfill(8)]

try:
    while True:
        a=input()
        if(a.isdigit()):
            a=int(a)
            if(0<=a<=255):
                GPIO.output(dac,func(a))
                print('Предполагаемое значение напряжения:',"{:.3f}".format((3.3/256*a)),'вольт')
            if(a<0):
                print('Отрицательное число')
            if(a>255):
                print('Число больше 255')
        
        else:
            print("Не число")
            print("Введите число от 0 до 255")

finally:
    GPIO.output(dac,0)
    GPIO.cleanup()    



