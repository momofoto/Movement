import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BCM)
PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
	current_time = datetime.datetime.now()
	print "Motion Detected"
	print current_time

print "Motion Detection Script" 
time.sleep(2)
print "Ready"

try:
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
        while 1:
                time.sleep(100)

except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()
