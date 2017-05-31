# rpi-projects


# Morse Code Buzzer:

This is a fun little project for the Raspberry Pi (in my case, v.3 running Raspian Jesse). It needs the rpi_gpio gem, but that's all. It could easily be done with pi_piper as well, but I was having a lot of dependency issues trying to add that it, so I just switched to rpi_gpio. 

From the User's end: When the script is run it asks the user "what message would you like to transmit?", then converts the string into morse code and beeps a "dit," "dah," or a pause, accordingly. When the transmission finishes, the script notifies the user: "Transmission sent" and exits. 

Technical details: The morse code values for the entire alphabet are hard coded into a hash in the script which is defined immediately after the GPIO pins are setup. There's also a commented-out option for LEDs to accompany or replace the active buzzer (good for nighttime coding courtesy). Everything works just as you might expect: the message is captured and stored as a string which gets broken down into an array of words, then letters. Each letter is individually translated to its morse equivalent in dits (".") and dahs ("-"), and stored in an array of such values. This array is eventually joined and passed into a transmit method which iterates through each series of morse values and activates the buzzer (and/or LEDs) for the appropriate amount of time. Once the script finishes running, it 'cleans' the pins before exiting (sets the voltage to low).

There's one maneuver that's perhaps a bit unexpected: rather than having the #buzz method tap each GPIO pin individually (requiring an awful lot of typing given the gem's syntactical structure), it passes the pin number into a pair of #activate / #deactivate methods. Between these methods calls there's a sleep timer to enforce the duration of the buzz. This not saves times typing (as mentioned above), but it allows for a much broader range of behaviors: passing an array of pins to activate instead of one at a time, allows the programmer or technician to use a different set of GPIO pins with much easier maintenance (simply need to change the initial setup line pin value and arguments for the #activate / #deactivate calls. 


# Security (written in Python as opposed to all my other scripts in Ruby)
Libraries Required: gpiozero, time, os

This is a simple little script that I wrote out of necessity more than curiosity: I was having a continual problem with a roommate entering my room and rifling through my things, stealing my socks, and just generally being creepy. He would repeatedly deny it, despite my catching him (multiple times) walking out of my room as just as I was entering the house. I needed undeniable proof. 

The program requires a Rasp Pi with a webcam attached via USB (I'm not sure if it will work with a ribbon cable camera module), and a breadboard with a photoresistor circuit with a 1uF capacitor. It works by checking the ambient light level in the room every second via the light-dependent resistor (LDR / photoresistor) against a pre-calibrated "lights off" reading. If the ambient light value exceeds the normal value, the webcam snaps a pic. 

The only tricky thing about this very simple script is the logistics. It can be tough to find that exact right reading where a passing car doesn't set it off, but someone opening the door without turning on the lights does. Also, I've instructed the webcam to wait 2 seconds before taking the picture, otherwise it would catch a snap of the door mid-opening and not the intruder's face, but your mileage may vary. 

Are you still reading this and wondering if it worked? Absolutely it did--the look on his face! Ashamed, confused, but also sort of impressed--it was amazing. In fact, this was one of the first times I used physical computing / IoT solutions of my own design to solve a real problem in my life.
