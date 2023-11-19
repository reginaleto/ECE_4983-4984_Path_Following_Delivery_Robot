import RPi.GPIO as GPIO
import time

# returns True to indiciate that a barcode has been detected
def Sensor_Output():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN)

    while True: 
        if GPIO.input(27) == 1: 
            break

    return True

if __name__ == '__main__':
    Sensor_Output() 