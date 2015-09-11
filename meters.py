'''This is my First attempt to use Raspberry Pi B+ as electromechanical meter reader.

The main challenges:
1) They are really fast (up to 10 impulses in a second)
2) The are on 12V board - I need to solve how to connect them and not to burn the RPi

	Opto-coupler will be used. PIN 1 to PIN 6

'''

import RPi.GPIO as GPIO            	# importing GPIO 
GPIO.setmode(GPIO.BOARD)			# setting that we use Board numbering of pins
GPIO.setup(18, GPIO.IN)				# setting pin 18 as an input
GPIO.cleanup ()
loop1 = True





'''MAIN PROGRAM LOOP'''
while loop1 == TRUE:
	if GPIO.input(18) == True:
		print "Counting ... "
		x = 1
		y = y + X
		print y



			
