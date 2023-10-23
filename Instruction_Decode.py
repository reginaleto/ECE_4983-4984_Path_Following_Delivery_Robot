import cv2
from picamera2 import Picamera2, Preview
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np
import time

# first barcode scanned should be loading station barcode
# first scan of loading station should be bypassed 
scan_count = 0

def Camera_Enable(camera):
    config = camera.create_preview_configuration()
    camera.configure(config)
    camera.start_preview(Preview.QTGL)
    camera.start()
    time.sleep(3)
    camera.capture_file("/home/ginaleto/Desktop/Barcodes/Detected_Barcode.png")
     

def Barcode_Decode():

    image = Image.open('/home/ginaleto/Desktop/Barcodes/Detected_Barcode.png')
    d = decode(image)

    # extracts data (barcode number) and prints
    for i in d: 
        #print(i.data.decode('utf-8'))
        barcode_id = i.data.decode('utf-8')
        # print(type(barcode_id)) # -- determine the type of the barcode ID *** 
        # print('\n' + barcode_id)
    
    scan_count = scan_count + 1 
    return barcode_id
    
def Instruction_Algorithm( self ):

    # first barcode in path -- main intersection
    if '1' in self.ID:
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'blue': 
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'green': 
                # Motor_Control.Keep_Straight()
        elif self.Payload_Color == None: 
            if self.Previous_Color == 'green': 
                # Motor_Control.Keep_Straight()
            if self.Previous_Color == 'red' or self.Previous_Color == 'blue': 
                # Motor_Control.Turn_Right()

    # barcode labeled #2
    elif '2' in self.ID: 
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                # Motor_Control.Turn_Right()
            elif self.Payload_Color == 'blue': 
                # Motor_Control.Turn_Right()
            elif self.Payload_Color == 'green': 
                # Motor_Control.Turn_Right()
        elif self.Payload_Color == None: 
            # Motor_Control.Turn_Left()
                
    # barcode labeled #3 
    elif '3' in self.ID: 
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'blue': 
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'green': 
                # do nothing
                pass
        elif self.Payload_Color == None: 
                # Motor_Control.Turn_Right()
                
    # barcode labeled #4 -- intersection for blue and red          
    elif '4' in self.ID: 
        if self.Payload_Color != None: 
            if self.Payload_Color == 'red':
                # Motor_Control.Turn_Left()
            elif self.Payload_Color == 'blue': 
                # Motor_Control.Turn_Right()
            elif self.Payload_Color == 'green': 
                # do nothing
                pass
        elif self.Payload_Color == None: 
                if self.Previous_Color == 'blue': 
                    # Motor_Control.Turn_Left()
                elif self.Previous_Color == 'red': 
                    # Motor_Control.Turn_Right()
                
    # barcode for dropping payload -- in front of each destination         
    elif '5' in self.ID: 
        # Payload_Manipulation.Bring_Down()
        self.Previous_Color = self.Payload_Color 
        self.Payload_Color = None 
        # Motor_Control.Turn_Left/Right() -- want to just turn 180deg
        
    # barcode at loading station 
    # is bypassed the first scan b/c no need to do anything when first payload is already picked up
    elif '6' in self.ID: 
        if scan_count > 1: 
            # Payload_Detect()
            # Payload_Manipulation.Bring_Up()
            # Motor_Control.Turn_Left/Right() -- want to just turn 180deg
            # Motor_Control.Move_Forward()
        elif scan_count <= 1: 
            pass 
    
def Camera_Disable(camera):
    camera.close()


def Main(self):
    # Motor_Control.Stop_Movement() -- either here or Sensor_Integration for Reflectance Sensors
  
    camera = Picamera2()
    Camera_Enable(camera)
    Camera_Disable(camera)

    self.ID = Barcode_Decode()
    Instruction_Algorithm(self)


if __name__ == '__main__':
    Main()
    
    