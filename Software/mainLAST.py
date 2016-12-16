import sys
import time
import RPi.GPIO as GPIO

#PIN numbers
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

def reverse():
	print "FORWARD"
	GPIO.output(StepPinForward1, GPIO.HIGH)
	GPIO.output(StepPinForward2, GPIO.HIGH)
	sleep(2)
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
	sleep(2)
	GPIO.output(StepPinBackward1, GPIO.LOW)
	GPIO.output(StepPinForward2, GPIO.LOW)

def left():
	print "LEFT"
	GPIO.output(StepPinForward1, GPIO.HIGH)
	GPIO.output(StepPinBackward2, GPIO.HIGH)
	sleep(2)
	GPIO.output(StepPinForward1, GPIO.LOW)
	GPIO.output(StepPinBackward2, GPIO.LOW)

while True:
#	readsensor(ECHOF)
#	readsensor(ECHOR)
#	readsensor(ECHOL)
#	forward()
	GPIO.cleanup()

	#L ja R on vaja muuta sleep ja lisada F, R PWM gpio
	#Kui küöjed lähedal siis kaskaadiga tagasi minnes kontrollib kuni avaneb
	#1. alati otse siis parem/vasak kummal rohkem dist 
	#SLEEP MANÖÖVRITE AJAL no data input