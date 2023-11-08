import RPi.GPIO as GPIO
import time
from subprocess import call

GPIO.setmode(GPIO.BCM)

IGN_PIN = 12
EN_POWER_PIN = 25

IGN_LOW_TIME = 10

GPIO.setup(IGN_PIN, GPIO.IN)

GPIO.setup(EN_POWER_PIN, GPIO.OUT, initial=GPIO.HIGH)

GPIO.output(EN_POWER_PIN, 1)

ignLowCounter = 0

while 1:
    if GPIO.input(IGN_PIN) != 1:
        time.sleep(1)
        ignLowCounter += 1
        if ignLowCounter > IGN_LOW_TIME:
            print("Shutting Down...")
            call("sudo shutdown -h now", shell=True)
    else:
        ignLowCounter = 0

time.sleep(0.1)
