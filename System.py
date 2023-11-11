import Instruction_Decode as Barcode
# import camera_adapter_test as camera_test
import Payload_Detection as Color_Detect
# import Payload_Manipulation as Forklift
# import Motor_Control as Motors
# import Streaming
# import Sensor_Integration as Sensor

import RPi.GPIO as GPIO

class System(): 
    def __init__(self):
        self.Payload_Color = "blue"
        self.Previous_Color = None
        self.ID = None

        # GPIO initialization for Cameras A and B on UC-444 adapter
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        # can NOT use IO4 or IO17 on GPIO HAT 
        GPIO.setup(4, GPIO.OUT) # camera A 
        GPIO.setup(17, GPIO.OUT) # camera B 
        print("****GPIO set****")
    

    def Main(self):
        
        # Color_Detect.Main(self)
        Barcode.Main(self)
        #Sensor.Main()

system_test = System()
system_test.Main()
    