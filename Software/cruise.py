#forward cruise control
import sys
import time
import RPi.GPIO as GPIO
import PID

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
ENCODERB=24
ENCODERA=23

GPIO.setup(ENCODERA, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(ENCODERB, GPIO.IN, GPIO.PUD_UP)
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

#WHEEL DIAMETER
WHEEL_DIAMETER=5

#navigation variables
reversetime=0
turningtime = 1
MAXSPEED = 90
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
current_time=0
last_time=0

#encoder values
CurRot = 0
Rotations = 0
Rev = 0
Last = 0
In = 0
Running = 1

pwmb.start(0)
pwma.start(0)

def reverse(SPEED):
	(GPIO.output(AIN1, GPIO.HIGH))
	(GPIO.output(AIN2, GPIO.LOW))
	(GPIO.output(BIN1, GPIO.HIGH))
	(GPIO.output(BIN2, GPIO.LOW))
	(GPIO.output(STBY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def forward(SPEEDA,SPEEDB):
	(GPIO.output(AIN1, GPIO.LOW))
	(GPIO.output(AIN2, GPIO.HIGH))
	(GPIO.output(BIN1, GPIO.LOW))
	(GPIO.output(BIN2, GPIO.HIGH))
	(GPIO.output(STBY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEEDA))
	(pwmb.ChangeDutyCycle(SPEEDB))

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
	(GPIOo.utput(STBY, GPIO.LOW))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def WheelA():
	global Rotate
	global CurRot
	global Running
	global Rotations
	global current_time
	global last_time
	CurRot = CurRot + 1
	sys.stdout.write(str(CurRot)+" ")
	sys.stdout.flush()
	if CurRot == 20 and Rotations == Rotate:
		off(0)
		print "\n{} Rotations!".format(Rotate+1)
		Running = 0
	elif CurRot == 20:
		current_time=time.time()
		wheel_speed=WHEEL_DIAMETER / (current_time - last_time)
		last_time=current_time
		Rotations = Rotations + 1
		sys.stdout.write("!\n")
		sys.stdout.flush()
		CurRot = 0
		return wheel_speedA

def WheelB():
	global Rotate
	global CurRot
	global Running
	global Rotations
	global current_time
	global last_time
	CurRot = CurRot + 1
	sys.stdout.write(str(CurRot)+" ")
	sys.stdout.flush()
	if CurRot == 20 and Rotations == Rotate:
		off(0)
		print "\n{} Rotations!".format(Rotate+1)
		Running = 0
	elif CurRot == 20:
		current_time=time.time()
		wheel_speed=WHEEL_DIAMETER / (current_time - last_time)
		last_time=current_time
		Rotations = Rotations + 1
		sys.stdout.write("!\n")
		sys.stdout.flush()
		CurRot = 0
		return wheel_speedB


forward(MINSPEED,MINSPEED)
while Running:
	InA = GPIO.input(ENCODERA)
	if GPIO.input(ENCODERA) == 0 and LastA == 1:
		WheelA()
	LastA = InA

	InB = GPIO.input(ENCODERB)
	if GPIO.input(ENCODERB) == 0 and LastB == 1:
		WheelB()
	LastB = InB

	forward(MINSPEED,MINSPEED-PID(wheel_speedA,wheel_speedB))
GPIO.cleanup()