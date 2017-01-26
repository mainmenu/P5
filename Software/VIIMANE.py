import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


#Pin numbers
PWMA = 19
AIN1 = 12
AIN2 = 5
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

pwma=GPIO.PWM(19,100)
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
sensorF_data = 0
sensorR_data = 0
sensorL_data = 0
pulse_end=1
pulse_start=2


pwmb.start(0)
pwma.start(0)

def readsensor(PIN):
	global sensorF_data
	global sensorR_data
	global sensorF_data
	print"Sensoralgab"
	for x in range(0, 2):
		read_time_start1 = time.time()
		GPIO.output(TRIG, True)
		time.sleep(pulse)
		GPIO.output(TRIG, False)

		while GPIO.input(PIN)==0:
			pulse_start = time.time()

		
		while GPIO.input(PIN)==1:
			pulse_end= time.time()

		pulse_duration[x] = pulse_end - pulse_start
		time.sleep(0.05-(time.time()-read_time_start1))

		
	distance = sum(pulse_duration)/measurment_count* SPEED_OF_SOUND
	distance = round(distance, 2)
	
	print distance
	
	if PIN == ECHOF:
		print "FRONT SENSOR"
		sensorF_data=distance
		return sensorF_data

	if PIN == ECHOR:
		print "RIGHT SENSOR"
		
		return sensorR_data

	if PIN == ECHOL:
		print "LEFT SENSOR"
		return sensorL_data


def reverse(SPEED):
	(GPIO.output(AIN1, GPIO.HIGH))
	(GPIO.output(AIN2, GPIO.LOW))
	(GPIO.output(BIN1, GPIO.HIGH))
	(GPIO.output(BIN2, GPIO.LOW))
	(GPIO.output(STBY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def forward(SPEED):
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

	



	print "hakkab pihta"
	readsensor(ECHOF)
	print "PEALE MOOTMIST LOOBIS" 
	print sensorF_data
	

	if sensorF_data>200:
		forward(MAXSPEED)
		print"maxspeed"
		
		
	if 200 > sensorF_data > 100:
		forward(MEDSPEED)
		print"medspeed"
		

	if 100>sensorF_data > 20:
		forward(MINSPEED)
		print "minspeed"
		

	if 20>sensorF_data:
		off(0)
		readsensor(ECHOR)
		
		readsensor(ECHOL)
		print"sein"

		while sensorR_data<15 and sensorL_data<15:	
			reverse(MINSPEED)
			readsensor(ECHOR)
			readsensor(ECHOL)
			
		if sensorR_data>sensorL_data== True:
			right(1,MINSPEED)
			
			
		if sensorL_data>sensorR_data==True:
			left(1,MINSPEED)
			

