import time
from subprocess import call


def turn_bluetooth_on():
    time.sleep(3)
    call("bluetoothctl connect XX:XX:XX:XX:XX:XX", shell=True)
    print("Connected to car bluetooth!")


turn_bluetooth_on()
