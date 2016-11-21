import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 18
ECHO2 = 23
ECHO3 = 24
ECHO4 = 25

print "Measuring distance"

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(ECHO3, GPIO.IN)
GPIO.setup(ECHO4, GPIO.IN)

while True:
	GPIO.output(TRIG, False)
	print "W8ing on da sensor2"
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO2)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO2)==1:
		pulse_end= time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)

	print "Distance2:%d",distance

	GPIO.output(TRIG, False)
	print "W8ing on da sensor3"
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO3)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO3)==1:
		pulse_end= time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)

	print "Distance3:%d",distance

	GPIO.output(TRIG, False)
	print "W8ing on da sensor4"
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO4)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO4)==1:
		pulse_end= time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)

	print "Distance4:%d",distance