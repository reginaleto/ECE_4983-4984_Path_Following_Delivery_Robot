import cv2
from picamera2 import Picamera2, Preview
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np
import time
import os
import RPi.GPIO as GPIO
import threading
from libcamera import controls
import Stae_Machine_Lf as Motors
import Payload_Manipulation as Forklift

# want camera A (i2c [1,0])

# first barcode scanned should be loading station barcode
# first scan of loading station should be bypassed 
scan_count = 0

camera_adapter_info = {  
    # A is camera for color detection (regular)
    "A" : {   
        "i2c_cmd":"i2cset -y 1 0x70 0x00 0x01",
        "gpio_sta":[0,0],
    }, 
    # B is camera for barcodes (wide)
    "B" : {
        "i2c_cmd":"i2cset -y 1 0x70 0x00 0x02",
        "gpio_sta":[1,0],
    }
}

def set_channel(index):
    # from select_channel
    channel_info = camera_adapter_info.get(index)
    if channel_info == None:
        print("Can't get this info")
    gpio_sta = channel_info["gpio_sta"] # gpio write
    GPIO.output(4, gpio_sta[0])
    GPIO.output(17, gpio_sta[1])

def init_i2c(index):  
    # from I2C_init 
    channel_info = camera_adapter_info.get(index)
    os.system(channel_info["i2c_cmd"]) # i2c write


def Camera_Enable(camera):
        camera.configure(camera.create_preview_configuration())
        camera.start(show_preview=True)
        camera.set_controls({"AfMode": controls.AfModeEnum.Continuous,"AeEnable":False,"ExposureTime":30000,"AnalogueGain":6})
        camera.capture_array("main", wait=True)

def Barcode_Decode():
    image = Image.open('/home/ginaleto/Desktop/Barcodes/Detected_Barcode.png')
    d = decode(image)

    # extracts data (barcode number) and prints
    for i in d: 
        barcode_id = i.data.decode('utf-8')
    
    #scan_count = scan_count + 1 
    return barcode_id
    
def Instruction_Algorithm( self ):
    global scan_count

    # first barcode in path -- main intersection
    if '11116' in self.ID: # 16 b/c extra char at end of barcode
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                print("red, left")
                Motors.Turn_Left()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
            elif self.Payload_Color == 'blue': 
                print("blue, left")
                Motors.Turn_Left()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
            elif self.Payload_Color == 'green':
                print("green, straight")
                # keep line following
                pass
        elif self.Payload_Color == None: 
            if self.Previous_Color == 'green': 
                print("reverse - green, straight")
                # keep line following
                pass
            if self.Previous_Color == 'red' or self.Previous_Color == 'blue': 
                print("reverse - red and blue, right")
                Motors.Turn_Right()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
        return False

    # barcode labeled #2
    elif '2' in self.ID: 
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                print("red, right")
                Motors.Turn_Right()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
            elif self.Payload_Color == 'blue': 
                print("blue, right")
                Motors.Turn_Right()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
            elif self.Payload_Color == 'green': 
                print("green, right")
                Motors.Turn_Right()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
        elif self.Payload_Color == None: 
            print("reverse")
            Motors.Turn_Left()
            time.sleep(1) # delay depends on weight
            Motors.Stop()
        return False
                
    # barcode labeled #3 
    elif '3' in self.self.ID: 
        if self.self.Payload_Color != None: 
            if self.self.Payload_Color == 'red':
                print("red, left")
                Motors.Turn_Left()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
            elif self.self.Payload_Color == 'blue': 
                print("blue, left")
                """ Motors.Turn_Left()
                time.sleep(1) # delay depends on weight
                Motors.Stop() """
            elif self.self.Payload_Color == 'green': 
                # do nothing
                pass
        elif self.self.Payload_Color == None: 
            print("reverse")
            Motors.Turn_Right()
            time.sleep(1) # delay depends on weight
            Motors.Stop()
        return False
                
    # barcode labeled #4 -- intersection for blue and red          
    elif '4' in self.ID: 
        if self.self.Payload_Color != None: 
            if self.self.Payload_Color == 'red':
                print("red, left")
                Motors.Turn_Left()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
            elif self.self.Payload_Color == 'blue': 
                print("blue, right")
                Motors.Turn_Right()
                time.sleep(1) # delay depends on weight
                Motors.Stop()
            elif self.self.Payload_Color == 'green': 
                # do nothing
                pass
        elif self.self.Payload_Color == None: 
                if self.Previous_Color == 'blue': 
                    print("reverse - blue, left")
                    Motors.Turn_Left()
                    time.sleep(1) # delay depends on weight
                    Motors.Stop()
                elif self.Previous_Color == 'red': 
                    print("reverse - red, right")
                    Motors.Turn_Right()
                    time.sleep(1) # delay depends on weight
                    Motors.Stop()
        return False
                
    # barcode for dropping payload -- in front of each destination         
    elif '5' in self.ID:
        Forklift.Motor_init() 
        Forklift.Bring_Down()
        print("bringing payload down")
        self.Previous_Color = self.self.Payload_Color 
        self.self.Payload_Color = None 
        print("left")
        # heavier loads require longer time.sleep time 
        if self.Previous_Color == 'red':
            Motors.Turn_Left() # -- want to just turn 180deg
            time.sleep(1) # delay depends on weight 
        elif self.Previous_Color == 'green':
            Motors.Turn_Left() # -- want to just turn 180deg
            time.sleep(1) # delay depends on weight 
        elif self.Previous_Color == 'blue':
            Motors.Turn_Left() # -- want to just turn 180deg
            time.sleep(1) # delay depends on weight 
        Motors.Stop()
        return False
        
    # barcode at loading station 
    # is bypassed the first scan b/c no need to do anything when first payload is already picked up
    elif '6666' in self.ID: # 66 to decipher between barcodes 1 and 6
        scan_count += 1
        if scan_count >= 2:
            return True     
            Motors.motor_Init()
            Motors.Move_forward()
            time.sleep(1)
            Motors.Stop()
            Forklift.Motor_init() 
            Forklift.Bring_Up()
            # only do 180 if this is not the first time
            # barcode #6 is being scanned
            if scan_count > 1: 
                Motors.Turn_Right() # -- want to just turn 180deg
                time.sleep(1)
                Motors.Stop()
                # Motors.Move_forward() -- move into line following
        elif scan_count <= 1: 
            return False
            # if scan_count = 0, keep moving forward
            self.ID = None
            pass

def Main(self):
    # Motors.Stop() # -- either here or Sensor_Integration for Reflectance Sensors
    global camera
    
    """ GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT) # camera A 
    GPIO.setup(17, GPIO.OUT) # camera B  """
    
    for item in {"A", "B"}: 
        if item == "A": 
            set_channel(item)
            init_i2c(item)
            camera = Picamera2()
            time.sleep(0.5)
            Camera_Enable(camera)
            time.sleep(5)
            camera.capture_file("/home/ginaleto/Desktop/Barcodes/Detected_Barcode.png") 
            camera.stop_preview()
            camera.stop()
        else: 
            continue

    self.ID = Barcode_Decode()
    print(self.ID)
    # RestartFlag = Instruction_Algorithm(self) 

    Instruction_Algorithm(self)
    # only perform turning instructions
    # in System.py, go back into line following

    # return RestartFlag 

if __name__ == '__main__':
    Main()