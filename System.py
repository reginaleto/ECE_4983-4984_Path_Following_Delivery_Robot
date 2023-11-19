import Instruction_Decode as Barcode_Detect
# import Payload_Detection as Color_Detect
import Color_Detection_Test as Payload_Detect
import Payload_Manipulation as Forklift
import Stae_Machine_Lf as Motors
import Sensor_Integration as IRSensor
# import Streaming
# import Sensor_Integration as Sensor

import time
import threading

import RPi.GPIO as GPIO

class System(): 
    def __init__(self):
        self.Payload_Color = None
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
        # Payload_Detect.color_detect(self)
        # print("self.Payload_Color: ", self.Payload_Color)
        Motors.motor_Init()
        Motors.Turn_Right()
        time.sleep(1.5)
        Motors.Stop()
        #Forklift.Motor_init()
        #Forklift.Bring_Up()
        # time.sleep(0.5)
        # Motors.Stop()
        # Barcode_Detect.Main(self)

        while True: 
            # initialize individual threads for line following and sensor integration
            barcode_detection = threading.Thread(target=IRSensor.Sensor_Output)
            line_following = threading.Thread(target = Motors.Line_Following)
            
            # start detecting color
            self.Payload_Color = Payload_Detect.color_detect(self) 
            
            # if color has been detected, start line following and start searching for barcodes in path
            while self.Payload_Color != None: 
                # start Line Following
                line_following.start() # line following is independent from barcode detection
                IRBarcodeFlag = barcode_detection.start() # barcode detection is independent from line following
                # IRBarcodeFlag = IRSensor.Sensor_Output()
                # stop motors if IR sensor detects barcode
                if IRBarcodeFlag == True: 
                    Motors.Stop()
                    Barcode_Detect.Main(self)
                    # break out of inner WHILE loop if loading station barcode was scanned
                    # keep looping if any other barcode is detected
                    if '66' in self.ID:   
                        self.Payload_Color = None # reset Payload_Color to break out of loop
            
system_test = System()
system_test.Main()
    