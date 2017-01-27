#PWM TESTS

import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


#Pin numbers
PWMA = 21
AIN1 = 26
AIN2 = 19
PWMB = 20
BIN1 = 13
BIN2 = 6
STBY = 16
ECHOF=4
ECHOL=27
ECHOR=22
TRIG=17


GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT) 
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)
GPIO.setup(ECHOF, GPIO.IN)
GPIO.setup(ECHOL, GPIO.IN)
GPIO.setup(ECHOR, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)

#PWM pins
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(PWMB, GPIO.OUT)

pwma=GPIO.PWM(21,100)
pwmb=GPIO.PWM(20,100)

#navigation variables
reversetime=0
turningtime = 1
MAXSPEED = 100
MEDSPEED = 70
MINSPEED = 50

#Values for reading the sesnsors
SPEED_OF_SOUND = 17150
measurment_count = 3
pulse = 0.00001	
pulse_duration = [0,0,0]
sensorF_data=0
sensorR_data=0
sensorL_data=0


pwmb.start(0)
pwma.start(0)

def forward(SPEED):
	(GPIO.output(AIN1, GPIO.HIGH))
	(GPIO.output(AIN2, GPIO.LOW))
	#(GPIO.output(BIN1, GPIO.HIGH))
	#(GPIO.output(BIN2, GPIO.LOW))
	(GPIO.output(STBY, GPIO.HIGH))
	#(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def reverse(SPEED):
	(GPIO.output(AIN1, GPIO.LOW))
	(GPIO.output(AIN2, GPIO.HIGH))
	(GPIO.output(BIN1, GPIO.LOW))
	(GPIO.output(BIN2, GPIO.HIGH))
	(GPIO.output(STBY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def left(SPEED):
	(GPIO.output(AIN1, GPIO.HIGH))
	(GPIO.output(AIN2, GPIO.LOW))
	(GPIO.output(BIN1, GPIO.LOW))
	(GPIO.output(BIN2, GPIO.HIGH))
	(GPIO.output(STBY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def right(SPEED):
	(GPIO.output(AIN1, GPIO.LOW))
	(GPIO.output(AIN2, GPIO.HIGH))
	(GPIO.output(BIN1, GPIO.HIGH))
	(GPIO.output(BIN2, GPIO.LOW))
	(GPIO.output(STBY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def off(SPEED):
	(GPIO.output(AIN1, GPIO.LOW))
	(GPIO.output(AIN2, GPIO.LOW))
	(GPIO.output(BIN1, GPIO.LOW))
	(GPIO.output(BIN2, GPIO.LOW))
	(GPIO.output(STBY, GPIO.LOW))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

while True:
	forward(MINSPEED)
	time.sleep(2)
	forward(MEDSPEED)
	time.sleep(2)
	forward(MAXSPEED)
	time.sleep(2)
	off(0)
	GPIO.cleanup