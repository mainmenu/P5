def measure(ECHO):
	GPIO.output(TRIG, False)
	print "W8ing on da sensor"
	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end= time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150
	distance = round(distance, 2)

	print "Distance:%d",distance

	return distance


def sendcommand(command):
	ser = serial.Serial('/dev/ttyACM0')

	ser.write(command)

	ser.close()

def turnleft():
	ser = serial.Serial('/dev/ttyACM0')
	ser.write(left)
	ser.close()

def turnright():
	ser = serial.Serial('/dev/ttyACM0')
	ser.write(right)
	ser.close()

def accelerate():
	ser = serial.Serial('/dev/ttyACM0')
	ser.write(moarpowa)
	ser.close()

def deaccelerate():
	ser = serial.Serial('/dev/ttyACM0')
	ser.write(lesspowa)
	ser.close()

def readstate():
	ser = serial.Serial('/dev/ttyACM0')
	carstate = ser.readline()
	ser.close()
	return carstate

def forward():
	ser = serial.Serial()