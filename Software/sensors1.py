
sensor_data1 = {
        "distance1": 0,
        "distance2": 0,
        "distance3": 0,
        "distance4": 0,
        "distance5": 0,
        "distance6": 0
}




def read_data1(sensorID,distance):
					                                      #Teha funktsioon nii et ex->read_data1() on parameeter sensorID
	SPEED_OF_SOUND = 17150
	measurment_count = 3
	pulse = 0.00001	
	pulse_duration = [0,0,0]
	for x in range(0, 2):
		GPIO.output(TRIG, True)
		time.sleep(pulse)
		GPIO.output(TRIG, False)

		while GPIO.input(sensorID)==0:
			pulse_start1 = time.time()

		while GPIO.input(sensorID)==1:
			pulse_end1= time.time()

		pulse_duration[x] = pulse_end - pulse_start
		time.sleep(0.05)

	distance = sum(pulse_duration)/measurment_count* SPEED_OF_SOUND
	distance = round(distance, 2)
	
while True:
	read_data1(ECHO1,distance1)
	read_data1(ECHO2,distance2)
	read_data1(ECHO3,distance3)
	read_data1(ECHO4,distance4)
	read_data1(ECHO5,distance5)
	read_data1(ECHO6,distance6)

	sensor_data1["distance1"]=distance1
	sensor_data1["distance2"]=distance2
	sensor_data1["distance3"]=distance3
	sensor_data1["distance4"]=distance4
	sensor_data1["distance5"]=distance5
	sensor_data1["distance6"]=distance6

	return sensor_data1

if __name__ == "__main__":
    print(read_data())





#kuidas teha 6 tsüklit, kas main.py v sensor sees ja mis moodi for?