import Instruction_Decode as Barcode_Detection
import Color_Detection_Test as Payload_Detect
import Payload_Manipulation as Forklift
import Stae_Machine_Lf as Motors
import Sensor_Integration as IRSensor

import time
import threading

import RPi.GPIO as GPIO

payload_detected = 0
         

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

    def Path_Following_Delivery_Sequence(self): 
    
        while True: 
            # initialize individual threads for line following and sensor integration
            barcode_detection = threading.Thread(target=IRSensor.Sensor_Output)
            line_following = threading.Thread(target = Motors.Line_Following)
            
            # start detecting color
            self.Payload_Color = Payload_Detect.color_detect(self) 
            payload_detected += 1
            # if color has been detected, pick up payload
            # if first payload, move forward only
            # if second and third payloads, turn 180deg before moving forward
            Motors.motor_Init()
            Motors.Move_forward()
            time.sleep(0.5)
            Motors.Stop()
            Forklift.Motor_init()
            Forklift.Bring_Up()
            
            if payload_detected == 1: 
                # do nothing
                # move into line following
                pass
            elif payload_detected > 1: 
                # first turn 180deg
                Motors.Turn_Left()
                time.sleep(5)
                Motors.Stop()
                pass

            # once payload has been picked up, start line following and start searching for barcodes in path
            while self.Payload_Color != None: 
                # start Line Following
                line_following.start() # line following is independent from barcode detection
                IRBarcodeFlag = barcode_detection.start() # barcode detection is independent from line following
                # IRBarcodeFlag = IRSensor.Sensor_Output()
                # stop motors if IR sensor detects barcode
                if IRBarcodeFlag == True: 
                    Motors.Stop()
                    RestartFlag = Instruction_Decode.Main(self)
                    # break out of inner WHILE loop if loading station barcode was scanned
                    # keep looping if any other barcode is detected
                    if RestartFlag == True:   
                        self.Payload_Color = None # reset Payload_Color to break out of loop
    

    def Main(self):
        global payload_detected
    
        self.Payload_Color = Payload_Detect.color_detect(self) 
        print(self.Payload_Color)
        

        Motors.motor_Init()
        Motors.Move_forward()
        time.sleep(2.5)
        Motors.Stop()
        time.sleep(0.5)

        Forklift.Motor_init()
        Forklift.Bring_Up()

        time.sleep(1)

        barcode_detection = threading.Thread(target=IRSensor.Sensor_Output)
        line_following = threading.Thread(target = Motors.Move_forward)
        barcode_detection.start()
        line_following.start() # thread is finished when barcode is detected in path
        
        barcode_detection.join(timeout=5)

        while barcode_detection.is_alive(): 
            barcode_detection.join(timeout=0.5) 
        
        
        Barcode_Detection.Main(self)
        Forklift.Bring_Down()

        # Motors.Stop()
        # Barcode_Detect.Main(self)


        # Payload_Detect.color_detect(self)
        # print("self.Payload_Color: ", self.Payload_Color) 

        
"""         Motors.motor_Init()
        Motors.Move_forward()
        time.sleep(0.7)
        Motors.Stop()
        time.sleep(1)
        Forklift.Motor_init()
        Forklift.Bring_Up()
        Motors.Move_forward()
        time.sleep(10)
        Motors.Stop()
        Forklift.Bring_Down()
        Motors.Move_Backward() """
        




system_test = System()
system_test.Main()
# system_test.Path_Following_Delivery_Sequence()
    