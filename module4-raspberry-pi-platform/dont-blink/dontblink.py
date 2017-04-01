import RPi.GPIO as GPIO
import time

# setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21,GPIO.OUT)
#message
print("Here we go! Press CTRL+C to exit")


while True:
    if GPIO.input(18):
        GPIO.output(21,False)
        time.sleep(0.5)
        GPIO.output(21,True)
        time.sleep(0.5)
    else:
        GPIO.output(21,True)
        time.sleep(0.2)
