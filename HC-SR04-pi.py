#!/usr/bin/python2.7
import RPi.GPIO as GPIO
import time

#VCC - 5V
#GND - GND

#trigger - pin 11
PIN_OUT = 11
#echo - pin 12
PIN_IN  = 12

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_OUT, GPIO.OUT) 
    GPIO.setup(PIN_IN, GPIO.IN)
    GPIO.output(PIN_OUT, GPIO.LOW)
    time.sleep(2)

def getTime():
    #give HC-SR04 a short 10uS pulse to trigger the module
    GPIO.output(PIN_OUT, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_OUT, GPIO.LOW)

    #caculate the length of time of high pulse 
    while GPIO.input(PIN_IN) == 0:
        start = time.time()
    while GPIO.input(PIN_IN) == 1:
        end = time.time()
    return end - start

def getDistance():
    distance = getTime() * 17150
    distance = round(distance, 2)
    return distance

def end_program(signal, frame):
    print "Ctrl+c to quit the program"
    GPIO.cleanup()   

if __name__ == '__main__':
    setup()
    while True:
        distance = getDistance()
        print distance, "cm"
        time.sleep(1)
