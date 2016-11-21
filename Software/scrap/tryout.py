SPEED_OF_SOUND = 17150
measurment_count = 3
pulse = 0.00001	
pulse_duration = [0,0,0]
for x in range(0, 2):
	GPIO.output(TRIG, True)
	time.sleep(pulse)
	GPIO.output(TRIG, False)

	while GPIO.input(ECHO1)==0:
		pulse_start1 = time.time()

	while GPIO.input(ECHO1)==1:
		pulse_end1= time.time()

	pulse_duration[x] = pulse_end - pulse_start
	time.sleep(0.05)

distance1 = sum(pulse_duration)/measurment_count* SPEED_OF_SOUND
distance1 = round(distance1, 2)