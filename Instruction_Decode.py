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
        print(barcode_id)

    return barcode_id
    
# def Instruction_Algorithm(barcode_id):
    
    
    
def Camera_Disable(camera):
    camera.close()



def Main(self):
    camera = Picamera2()
    Camera_Enable(camera)
    Camera_Disable(camera)

    self.ID = Barcode_Decode()


if __name__ == '__main__':
    Main()
    
    