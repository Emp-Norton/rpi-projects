# rpi-projects


# Morse Code Buzzer:

This is a fun little project for the Raspberry Pi (in my case, v.3 running Raspian Jesse). It needs the rpi_gpio gem, but that's all. It could easily be done with pi_piper as well, but I was having a lot of dependency issues trying to add that it, so I just switched to rpi_gpio. 

From the User's end: When the script is run it asks the user "what message would you like to transmit?", then converts the string into morse code and beeps a "dit," "dah," or a pause, accordingly. When the transmission finishes, the script notifies the user: "Transmission sent" and exits. 

Technical details: The morse code values for the entire alphabet are hard coded into a hash in the script which is defined immediately after the GPIO pins are setup. There's also a commented-out option for LEDs to accompany or replace the active buzzer (good for nighttime coding courtesy). Everything works just as you might expect: the message is captured and stored as a string which gets broken down into an array of words, then letters. Each letter is individually translated to its morse equivalent in dits (".") and dahs ("-"), and stored in an array of such values. This array is eventually joined and passed into a transmit method which iterates through each series of morse values and activates the buzzer (and/or LEDs) for the appropriate amount of time. Once the script finishes running, it 'cleans' the pins before exiting (sets the voltage to low).

There's one maneuver that's perhaps a bit unexpected: rather than having the #buzz method tap each GPIO pin individually (requiring an awful lot of typing given the gem's syntactical structure), it passes the pin number into a pair of #activate / #deactivate methods. Between these methods calls there's a sleep timer to enforce the duration of the buzz. This not saves times typing (as mentioned above), but it allows for a much broader range of behaviors: passing an array of pins to activate instead of one at a time, allows the programmer or technician to use a different set of GPIO pins with much easier maintenance (simply need to change the initial setup line pin value and arguments for the #activate / #deactivate calls. 
