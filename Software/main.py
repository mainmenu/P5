import time
import RPi.GPIO as GPIO
import sensors1
import sensors2 #MUST MAKE
GPIO.setmode(GPIO.BCM)

TRIG = 18
ECHO1 = 23	
ECHO2 = 24
ECHO3 = 25
ECHO4 = 17
ECHO5 = 27
ECHO6 = 22

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.setup(ECHO3, GPIO.IN)
GPIO.setup(ECHO4, GPIO.IN)
GPIO.setup(ECHO5, GPIO.IN)
GPIO.setup(ECHO6, GPIO.IN)

def get_direction(sensor_data1):
	if sensor_data1["distance1"]> 70:
		return "forward3"
	if 70>sensor_data1["distance1"]>40:
		return "forward2"
	if 40>sensor_data1["distance1"]>20:
		return "forward1"
	if sensor_data1["distance1"]<20:
		return "STOP"


"""def get_turn(sensor_data2):
	if sensor_data2:                   MAKE AFTER WE GET LINE READING
        return "left"
    elif sensor_data2:
        return "right"""
def get_leftproximity(sensor_data1):
	if 20 < sensor_data1["distance4"] < 30
		return "left3"
	if 10 < sensor_data1["distance4"] < 20
		return "left2"
	if sensor_data1["distance4"] < 10
		return "left1"
def get_rightproximity(sensor_data1):
	if 20 < sensor_data1["distance5"] < 30
		return "right3"
	if 10 < sensor_data1["distance5"] < 20
		return "right2"
	if sensor_data1["distance5"] < 10
		return "right1"

def get_backproximity(sensor_data1):
	if sensor_data1["distance1"]> 70:
		return "forward3"
	if 70>sensor_data1["distance1"]>40:
		return "forward2"
	if 40>sensor_data1["distance1"]>20:
		return "forward1"
	if sensor_data1["distance1"]<20:
		return "STOP"

def create_command(sensor_data1,sensor_data2):
	command = {
        "direction": get_direction(sensor_data1),
        "leftproximity":get_leftproximity(sensor_data1),
        "rightproximity":get_rightproximity(sensor_data1),
        "backproximity":get_backproximity(sensor_data1),
        "turn": get_turn(sensor_data2),
        
    }

    print command
    return command

def send_command(sensor_data1,sensor_data2):

	"""Here ges the turning override if we get the line reading in order"""
	if command["direction"] == "forward3":
		ser = serial.Serial('/dev/ttyACM0')
		ser.write('13')
		ser.close()

	if command["direction"] == "forward2":
		ser = serial.Serial('/dev/ttyACM0')
		ser.write('12')
		ser.close()

	if command["direction"] == "forward1":
		ser = serial.Serial('/dev/ttyACM0')
		ser.write('11')
		ser.close()

while True:
	sensor_data1 = sensors1.read_data1()
	sensor_data2 = sensors2.read_data2()
    command = create_command(sensor_data1,sensor_data2)
    send_command(command)
	




	"""if lineread=True and linereadmarking1 and distance1 > setdistance3  :
		forward(3)

	#Make the car move forward w max speed
	
	if lineread=True and setdistance3 > distance1 > setdistance2:
		forward(2)

	if lineread=True and setdistance2> distance1> setdistance1:
		forward(1)

	if distance < setdistance1 :
		STOP()

	##Upper is the forward movement n different speeds according to the obstacle or not

	if linereadmarking1=True :
		#FIXED TURN FUNC
		"""
	
	