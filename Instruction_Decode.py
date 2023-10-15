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
        # print(type(barcode_id)) # -- determine the type of the barcode ID *** 
        # print('\n' + barcode_id)
    return barcode_id
    
def Instruction_Algorithm( color, barcode_id ):

    if color == 'red':
        if '1' in barcode_id:
            print("Color is red. ID is 1. Turn Left.")
        elif '2' in barcode_id: 
            print("Color is red. ID is 2. Turn Right.")
        elif '3' in barcode_id: 
            print("Color is red. ID is 3. Keep Straight.")
    
    if color == 'blue':
        if '1' in barcode_id:
            print("Color is blue. ID is 1. Keep Straight.")
        elif '2' in barcode_id: 
            print("Color is blue. ID is 2. Turn Left.")
        elif '3' in barcode_id: 
            print("Color is blue. ID is 3. Turn Right.")
        
    if color == 'green': 
        if '1' in barcode_id:
            print("Color is green. ID is 1. Turn Right.")
        elif '2' in barcode_id: 
            print("Color is green. ID is 2. Keep Straight.")
        elif '3' in barcode_id: 
            print("Color is green. ID is 3. Turn Left.")       
    
    
def Camera_Disable(camera):
    camera.close()


def Main(self):
    # Motor_Control.Stop_Movement() -- either here or Sensor_Integration for Reflectance Sensors
  
    camera = Picamera2()
    Camera_Enable(camera)
    Camera_Disable(camera)

    self.ID = Barcode_Decode()
    Instruction_Algorithm(self.Payload_Color, self.ID)


if __name__ == '__main__':
    Main()
    
    