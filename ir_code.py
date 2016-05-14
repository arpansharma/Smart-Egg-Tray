import RPi.GPIO as GPIO

import os
import sys
GPIO.setmode(GPIO.BCM)

GPIO.setup(10, GPIO.OUT)

GPIO.setup(15, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(4, GPIO.IN)

GPIO.output(10, True)

s = "python mail.py"

while 1:
        if GPIO.input(15) == 0 and GPIO.input(18) == 0 and GPIO.input(17) == 0:
                print "Combination 1"
                os.system(s)
                sys.exit()
        elif GPIO.input(15) == 0 and GPIO.input(18) == 0 and GPIO.input(4) == 0:
                print "Combination 2"
                os.system(s)
                sys.exit()
        elif GPIO.input(15) == 0 and GPIO.input(17) == 0 and GPIO.input(4) == 0:
                print "Combination 3"
                os.system(s)
                sys.exit()
        elif GPIO.input(4) == 0 and GPIO.input(18) == 0 and GPIO.input(17) == 0:
                print "Combination 4"
                os.system(s)
                sys.exit()
        else:
                print "There is sufficient stock !"
