import cv2
from picamera2 import Picamera2, Preview
from pyzbar.pyzbar import decode
from PIL import Image
import numpy as np
import time

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
        # print(type(barcode_id)) -- determine the type of the barcode ID *** 

    return barcode_id
    
def Instruction_Algorithm( self ):
    if self.Payload_Color == 'red':
        if self.ID == 1:
            print("Color is red. ID is X. Turn Left.")
        elif self.ID == 2: 
            print("Color is red. ID is Y. Turn Right.")
        elif self.ID == 3: 
            print("Color is red. ID is Z. Keep Straight.")
    if self.Payload_Color == 'blue':
        if self.ID == 1:
            print("Color is blue. ID is X. Keep Straight.")
        elif self.ID == 2: 
            print("Color is blue. ID is Y. Turn Left.")
        elif self.ID == 3: 
            print("Color is blue. ID is Z. Turn Right.")
        
    if self.Payload_Color == 'green': 
        if self.ID == 1:
            print("Color is green. ID is X. Turn Right.")
        elif self.ID == 2: 
            print("Color is green. ID is Y. Keep Straight.")
        elif self.ID == 3: 
            print("Color is green. ID is Z. Turn Left.")       
    
    
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
    
    