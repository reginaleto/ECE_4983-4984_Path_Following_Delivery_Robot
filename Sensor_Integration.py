import RPi.GPIO as GPIO
import time
import Stae_Machine_Lf as Motors
import Instruction_Decode as Barcode
# returns True to indiciate that a barcode has been detected
def Sensor_Output():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(7, GPIO.IN)
    while True: 
        if GPIO.input(7) == 0:
            print(GPIO.input(7))
            print("Barcode Detected")
            #Motors.Stop()
            #break

if __name__ == '__main__':
    Sensor_Output() 