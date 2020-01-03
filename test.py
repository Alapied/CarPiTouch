import time

#GPIO.input(27) = var1
var1 = True
if var1:
	print('Ignition state detected')
else:
	print('Ignition state inactive yet pi is on')
	
while True:
	#GPIO.input(27) = var1
	var1 = input('TRUE FALSE')
	if not var1:
		print('Timer Start')
		max_limit = 5	# Seconds.
		start = time.time()
		while time.time() - start < max_limit:
			var1 = input('TRUE FALSE')
			#GPIO.input(27) = var1
			if var1:
				Ignon = True
				print('Ignition on')
			else:
				Ignon = False
				print('Ignition off')
		if Ignon == False:
			print('Ignition off off')
			
			break