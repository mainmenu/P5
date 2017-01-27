import time 
import socket 
import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
interval = 0.1
regularUpdate = True

# Set which GPIO pins the drive outputs are connected
PWMA = 21
AIN1 = 26
AIN2 = 19
PWMB = 20
BIN1 = 13
BIN2 = 6
STBY = 16
##
### Set all the drive pins as output pins
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT) 
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)


def forward():
	(GPIO.output(AIN1, GPIO.HIGH))
	(GPIO.output(AIN2, GPIO.LOW))
	(GPIO.output(BIN1, GPIO.HIGH))
	(GPIO.output(BIN2, GPIO.LOW))
	(GPIO.output(STBY, GPIO.HIGH))
	(GPIO.output(PWMA, GPIO.HIGH))
	(GPIO.output(PWMB, GPIO.HIGH))

def reverse():
	(GPIO.output(AIN1, GPIO.LOW))
	(GPIO.output(AIN2, GPIO.HIGH))
	(GPIO.output(BIN1, GPIO.LOW))
	(GPIO.output(BIN2, GPIO.HIGH))
	(GPIO.output(STBY, GPIO.HIGH))
	(GPIO.output(PWMA, GPIO.HIGH))
	(GPIO.output(PWMB, GPIO.HIGH))

def left():
	(GPIO.output(AIN1, GPIO.HIGH))
	(GPIO.output(AIN2, GPIO.LOW))
	(GPIO.output(BIN1, GPIO.LOW))
	(GPIO.output(BIN2, GPIO.HIGH))
	(GPIO.output(STBY, GPIO.HIGH))
	(GPIO.output(PWMA, GPIO.HIGH))
	(GPIO.output(PWMB, GPIO.HIGH))

def right():
	(GPIO.output(AIN1, GPIO.LOW))
	(GPIO.output(AIN2, GPIO.HIGH))
	(GPIO.output(BIN1, GPIO.HIGH))
	(GPIO.output(BIN2, GPIO.LOW))
	(GPIO.output(STBY, GPIO.HIGH))
	(GPIO.output(PWMA, GPIO.HIGH))
	(GPIO.output(PWMB, GPIO.HIGH))

def off():
	(GPIO.output(AIN1, GPIO.LOW))
	(GPIO.output(AIN2, GPIO.LOW))
	(GPIO.output(BIN1, GPIO.LOW))
	(GPIO.output(BIN2, GPIO.LOW))
	(GPIO.output(STBY, GPIO.LOW))
	(GPIO.output(PWMA, GPIO.LOW))
	(GPIO.output(PWMB, GPIO.LOW))


while True:
	print "TEST!!!!"

	forward()
	time.sleep(2)
	reverse()
	time.sleep(2)
	left()
	time.sleep(2)
	right()
	time.sleep(2)
	off()
