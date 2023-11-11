import RPi.GPIO as GPIO
import time

# does not work with GPIO BCM connected to same number on HAT & GPIO pins

def Main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(27, GPIO.IN)

    while True: 
        print(GPIO.input(27))
        time.sleep(0.5)

if __name__ == '__main__':
    Main() 