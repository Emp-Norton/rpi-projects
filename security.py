from gpiozero import LightSensor
import os 
import time 

ldr = LightSensor(18)
lumen_threshold = 0.7 # ambient light in my test environment, YMMV
while True:
	alv = ldr.value
	print("Security active")
	print("%s") % alv # not necessary, but helpful to ensure LDR is working
	time.sleep(1)
	if alv > lumen_threshold:
 		 time.sleep(0.2) # needs a delay between light and pic, otherwise photo is dark.
		 os.system("sudo fswebcam intruder")
		 print("Successful.") # unnecessary, but helpful during config. Good idea to remove before implementation.
		 break
