import cv2
from picamera2 import Picamera2, Preview
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np
import time
import os
import RPi.GPIO as GPIO
import threading

# want camera A (i2c [1,0])

# first barcode scanned should be loading station barcode
# first scan of loading station should be bypassed 
scan_count = 0

camera_adapter_info = {  
    # A is camera for barcodes (wide)
    "A" : {   
        "i2c_cmd":"i2cset -y 1 0x70 0x00 0x01",
        "gpio_sta":[0,0],
    }, 
    # B is camera for color detection (regular)
    "B" : {
        "i2c_cmd":"i2cset -y 1 0x70 0x00 0x02",
        "gpio_sta":[1,0],
    }
}

def set_GPIO():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.setup(11, GPIO.OUT)
    print("****GPIO set****")

def set_channel(index):
    # from select_channel
    channel_info = camera_adapter_info.get(index)
    print("****channel_info set to camera " + index + "****")
    if channel_info == None:
        print("Can't get this info")
    gpio_sta = channel_info["gpio_sta"] # gpio write
    print("****gpio_sta set to channel_info value****")
    GPIO.output(7, gpio_sta[0])
    GPIO.output(11, gpio_sta[1])
    print("****GPIO output pin set****")

def init_i2c(index):  
    # from I2C_init 
    channel_info = camera_adapter_info.get(index)
    print("****channel_info set with camera A****")
    os.system(channel_info["i2c_cmd"]) # i2c write
    print("*****I2C Complete****")


def Camera_Enable(camera):
        camera.configure(camera.create_preview_configuration(main={"size": (320, 240),"format": "BGR888"},buffer_count=2))
        print("****camera configured with config var****")
        camera.set_controls({"AeEnable":False,"ExposureTime":30000,"AnalogueGain":6})
        print("****controls set****")
        # camera.start_preview(Preview.QTGL)
        # print("****preview started****")
        camera.start()
        print("****camera started****")
        time.sleep(3)
        print("****slept for 3s****")
        camera.capture_array("main", wait=True)
        print("***captured array****")
        camera.capture_file("/home/ginaleto/Desktop/Barcodes/Detected_Barcode.png")
        print("****image of barcode captured****")

def Barcode_Decode():

    image = Image.open('/home/ginaleto/Desktop/Barcodes/Detected_Barcode.png')
    d = decode(image)

    # extracts data (barcode number) and prints
    for i in d: 
        #print(i.data.decode('utf-8'))
        barcode_id = i.data.decode('utf-8')
        # print(type(barcode_id)) # -- determine the type of the barcode ID *** 
        # print('\n' + barcode_id)
    
    #scan_count = scan_count + 1 
    return barcode_id
    
def Instruction_Algorithm( self ):

    # first barcode in path -- main intersection
    if '16' in self.ID: # 16 b/c extra char at end of barcode
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                print("red, left")
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'blue': 
                print("blue, left")
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'green': 
                # Motor_Control.Keep_Straight()
                print("green, straight")
        elif self.Payload_Color == None: 
            if self.Previous_Color == 'green': 
                print("reverse - green, straight")
                # Motor_Control.Keep_Straight()
            if self.Previous_Color == 'red' or self.Previous_Color == 'blue': 
                print("reverse - red and blue, right")
                # Motor_Control.Turn_Right()

    # barcode labeled #2
    elif '2' in self.ID: 
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                print("red, right")
                # Motor_Control.Turn_Right()
            elif self.Payload_Color == 'blue': 
                print("blue, right")
                # Motor_Control.Turn_Right()
            elif self.Payload_Color == 'green': 
                print("green, right")
                # Motor_Control.Turn_Right()
        elif self.Payload_Color == None: 
            print("reverse")
            # Motor_Control.Turn_Left()
                
    # barcode labeled #3 
    elif '3' in self.ID: 
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                print("red, left")
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'blue': 
                print("blue, left")
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'green': 
                # do nothing
                pass
        elif self.Payload_Color == None: 
            print("reverse")
                # Motor_Control.Turn_Right()
                
    # barcode labeled #4 -- intersection for blue and red          
    elif '4' in self.ID: 
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                print("red, left")
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'blue': 
                print("blue, right")
                # Motor_Control.Turn_Right()
            elif self.Payload_Color == 'green': 
                # do nothing
                pass
        elif self.Payload_Color == None: 
                if self.Previous_Color == 'blue': 
                    print("reverse - blue, left")
                    # Motor_Control.Turn_Left()
                elif self.Previous_Color == 'red': 
                    print("reverse - red, right")
                    # Motor_Control.Turn_Right()
                
    # barcode for dropping payload -- in front of each destination         
    elif '5' in self.ID: 
        # Payload_Manipulation.Bring_Down()
        print("bringing payload down")
        self.Previous_Color = self.Payload_Color 
        self.Payload_Color = None 
        print("left")
        # Motor_Control.Turn_Left/Right() -- want to just turn 180deg
        
    # barcode at loading station 
    # is bypassed the first scan b/c no need to do anything when first payload is already picked up
    elif '66' in self.ID: # 66 to decipher between barcodes 1 and 6
        if scan_count > 1: 
            print("detect payload")
            print("bringing payload up")
            print("turn")
            print("straight")
            # Payload_Detect()
            # Payload_Manipulation.Bring_Up()
            # Motor_Control.Turn_Left/Right() -- want to just turn 180deg
            # Motor_Control.Move_Forward()
"""         elif scan_count <= 1: 
            pass  """


def Main(self):
    # Motor_Control.Stop_Movement() -- either here or Sensor_Integration for Reflectance Sensors
    global camera
    set_GPIO()
    for item in {"A", "B"}: 
        # print(camera_adapter_info.index)
        if item == "B": 
            set_channel(item)
            init_i2c(item)
            print("****I2C init def completed****")
            print("init1"+item)
            camera = Picamera2()
            time.sleep(0.5)
            Camera_Enable(camera)
            camera.close()
            self.ID = Barcode_Decode()
            Instruction_Algorithm(self)
        else: 
            continue



if __name__ == '__main__':
    Main()
    
    