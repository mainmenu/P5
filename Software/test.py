#!/usr/bin/env python2.7

import sys
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Pin numbers
# first motor
A_PULSE_WIDTH_MODULATION = 19
A_IN_1 = 12
A_IN_2 = 5
# second motor
B_PULSE_WIDTH_MODULATION = 20
B_IN_1 = 13
B_IN_2 = 6

STAND_BY = 16

ECHO_FRONT = 4
ECHO_LEFT = 27
ECHO_RIGHT = 22

TRIGGER = 17

# setup pins
GPIO.setup(A_IN_1,     GPIO.OUT)
GPIO.setup(A_IN_2,     GPIO.OUT) 
GPIO.setup(B_IN_1,     GPIO.OUT)
GPIO.setup(B_IN_2,     GPIO.OUT)
GPIO.setup(STAND_BY,   GPIO.OUT)
GPIO.setup(ECHO_FRONT, GPIO.IN)
GPIO.setup(ECHO_LEFT,  GPIO.IN)
GPIO.setup(ECHO_RIGHT, GPIO.IN)
GPIO.setup(TRIGGER,    GPIO.OUT)

#PWM pins
GPIO.setup(A_PULSE_WIDTH_MODULATION, GPIO.OUT)
GPIO.setup(B_PULSE_WIDTH_MODULATION, GPIO.OUT)

# enable 100 hertz 
pwma = GPIO.PWM(19,100)
pwmb = GPIO.PWM(20,100)

#navigation variables
reversetime=0
turningtime = 1
MAX_SPEED = 100
MED_SPEED = 70
MIN_SPEED = 40

#Values for reading the sesnsors
SPEED_OF_SOUND = 17150
measurment_count = 3
pulse = 0.00001	
pulse_duration = [0,0,0]
sensor_distance = 0
sensor_right_distance = 0
sensor_left_distance = 0
pulse_end = 1
pulse_start = 2


pwmb.start(0)
pwma.start(0)

def readsensor(PIN):
	global pulse_end
	global pulse_start
	for x in range(0, 2):
		read_time_start1 = time.time()
		GPIO.output(TRIGGER, True)
		time.sleep(pulse)
		GPIO.output(TRIGGER, False)

		while GPIO.input(PIN)==0:
			pulse_start = time.time()

		
		while GPIO.input(PIN)==1:
			pulse_end= time.time()

		pulse_duration[x] = pulse_end - pulse_start
#		time.sleep(0.07-(time.time()-read_time_start1))

		
	distance = sum(pulse_duration) / measurment_count * SPEED_OF_SOUND
	distance = round(distance, 2)

        return distance

def reverse(SPEED):
	(GPIO.output(A_IN_1,   GPIO.HIGH))
	(GPIO.output(A_IN_2,   GPIO.LOW))
	(GPIO.output(B_IN_1,   GPIO.HIGH))
	(GPIO.output(B_IN_2,   GPIO.LOW))
	(GPIO.output(STAND_BY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def forward(SPEED):
	(GPIO.output(A_IN_1,   GPIO.LOW))
	(GPIO.output(A_IN_2,   GPIO.HIGH))
	(GPIO.output(B_IN_1,   GPIO.LOW))
	(GPIO.output(B_IN_2,   GPIO.HIGH))
	(GPIO.output(STAND_BY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def left(SPEED):
	(GPIO.output(A_IN_1,   GPIO.HIGH))
	(GPIO.output(A_IN_2,   GPIO.LOW))
	(GPIO.output(B_IN_1,   GPIO.LOW))
	(GPIO.output(B_IN_2,   GPIO.HIGH))
	(GPIO.output(STAND_BY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def right(SPEED):
	(GPIO.output(A_IN_1,   GPIO.LOW))
	(GPIO.output(A_IN_2,   GPIO.HIGH))
	(GPIO.output(B_IN_1,   GPIO.HIGH))
	(GPIO.output(B_IN_2,   GPIO.LOW))
	(GPIO.output(STAND_BY, GPIO.HIGH))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))

def off(SPEED):
	(GPIO.output(A_IN_1,   GPIO.LOW))
	(GPIO.output(A_IN_2,   GPIO.LOW))
	(GPIO.output(B_IN_1,   GPIO.LOW))
	(GPIO.output(B_IN_2,   GPIO.LOW))
	(GPIO.output(STAND_BY, GPIO.LOW))
	(pwma.ChangeDutyCycle(SPEED))
	(pwmb.ChangeDutyCycle(SPEED))


# moving state can be "FORWARD", "REVERSE", "LEFT", "RIGHT"
moving_state = "FORWARD" 
speed = MAX_SPEED

# main loop
while True:

        # update command
        if moving_state == "FORWARD":
                forward(speed)
        elif moving_state == "REVERSE":
                reverse(MIN_SPEED)
        elif moving_state == "LEFT":
                left(MIN_SPEED)
        elif moving_state == "RIGHT":
                right(MIN_SPEED)
        else:
                raise "persetes"
        

        sensor_front_distance = readsensor(ECHO_FRONT)
        sensor_right_distance = readsensor(ECHO_RIGHT)
        sensor_left_distance = readsensor(ECHO_LEFT)

        # update state
        if moving_state == "FORWARD":
                if sensor_front_distance > 200:         speed = MAX_SPEED
                elif 200 > sensor_front_distance > 100: speed = MED_SPEED
                elif 100 > sensor_front_distance > 20 : speed = MIN_SPEED
                else:
                        # kill engines for a moment
                        off(0) 
                        time.sleep(0.2)
                        moving_state = "REVERSE";
                        speed = MIN_SPEED

        elif moving_state == "REVERSE" :

                if sensor_right_distance < 15 and sensor_left_distance < 15:
                        moving_state = "REVERSE"
                else:
                        if sensor_left_distance < sensor_right_distance:
                                moving_state = "RIGHT"
                        else:
                                moving_state = "LEFT"
        elif moving_state == "LEFT" or "RIGHT":
                if sensor_front_distance > 20:
                        moving_state = "FORWARD"

        else:
                raise "PERSETES"
             
