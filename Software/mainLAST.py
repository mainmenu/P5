import sys
import time
import RPi.GPIO as GPIO

#PIN numbers
LetfPWM=
RightPWM=
StepPinForward1=26
StepPinBackward1=19
StepPinForward2=13
StepPinBackward2=6
ECHOF=4
ECHOL=27
ECHOR=22
TRIG=17


#Values for reading the sesnsors
SPEED_OF_SOUND = 17150
measurment_count = 3
pulse = 0.00001	
pulse_duration = [0,0,0]
sensorF_data=0
sensorR_data=0
sensorL_data=0

#navigation variables
reversetime=0
turningtime = 1
MAXSPEED = 1
MEDSPEED = 0.6
MINSPEED = 0.1

#GPIO setup for each pin 
GPIO.setmode(GPIO.BCM)
GPIO.setup(StepPinForward1, GPIO.OUT)
GPIO.setup(StepPinBackward1, GPIO.OUT)
GPIO.setup(StepPinForward2, GPIO.OUT)
GPIO.setup(StepPinBackward2, GPIO.OUT)
GPIO.setup(ECHOF, GPIO.IN)
GPIO.setup(ECHOL, GPIO.IN)
GPIO.setup(ECHOR, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)

def readsensor(PIN):
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
		sensorF_data=distance

	if PIN == ECHOR:
		sensorR_data=distance

	if PIN==ECHOL:
		sensorL_data=distance

def stop():
	GPIO.output(StepPinForward1, GPIO.LOW)
	GPIO.output(StepPinForward2, GPIO.LOW)


def reverse(reversetime):
	print "FORWARD"
	GPIO.output(StepPinForward1, GPIO.HIGH)
	GPIO.output(StepPinForward2, GPIO.HIGH)
	sleep(reversetime)
	GPIO.output(StepPinForward1, GPIO.LOW)
	GPIO.output(StepPinForward2, GPIO.LOW)

def forward():
	print "REVERSE"
	GPIO.output(StepPinBackward1, GPIO.HIGH)
	GPIO.output(StepPinBackward2, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(StepPinBackward1, GPIO.LOW)
	GPIO.output(StepPinBackward2, GPIO.LOW)

def right():
	print "RIGHT"
	GPIO.output(StepPinBackward1, GPIO.HIGH)
	GPIO.output(StepPinForward2, GPIO.HIGH)
	sleep(turningtime)
	GPIO.output(StepPinBackward1, GPIO.LOW)
	GPIO.output(StepPinForward2, GPIO.LOW)

def left():
	print "LEFT"
	GPIO.output(StepPinForward1, GPIO.HIGH)
	GPIO.output(StepPinBackward2, GPIO.HIGH)
	sleep(turningtime)
	GPIO.output(StepPinForward1, GPIO.LOW)
	GPIO.output(StepPinBackward2, GPIO.LOW)

while True:
#	readsensor(ECHOF)
#	readsensor(ECHOR)
#	readsensor(ECHOL)
#	forward()
	GPIO.cleanup()


	if sensorF_data>200:
		forward(MAXSPEED)
		
	if 200>sensorF_data>100:
		forward(MEDSPEED)

	if 100>sensorF_data>20:
		forward(MINSPEED)

	if 20>sensorF_data:
		stop()
		readsensor(ECHOR)
		readsensor(ECHOL)
		if sensorR_data<15 and sensorL_data<15:
			reverse(1)
			break
		if sensorR_data>sensorL_data== True:
			right()
			break
		if sensorL_data>sensorR_data==True:
			left()
			break


	#-L ja R on vaja muuta sleep ja lisada F, R PWM gpio
	#-Kui küöjed lähedal siis kaskaadiga tagasi minnes kontrollib kuni avaneb
	#-1. alati otse siis parem/vasak kummal rohkem dist 
	#-SLEEP MANÖÖVRITE AJAL no data input
	#-iga sensori väljund eraldi returniga
	#-viimane loogika on ikka putsis
	