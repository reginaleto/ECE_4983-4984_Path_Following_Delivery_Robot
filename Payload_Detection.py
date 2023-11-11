# Is there a way for it to output without exiting the frame? Yes
# 

import os
import cv2
from picamera2 import Picamera2
import numpy as np
import time
import RPi.GPIO as GPIO
from libcamera import controls

duration = 5

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

lower_red = np.array([126, 188, 47])  # lower and upper bounds to detect red color
upper_red = np.array([179, 255, 255])

lower_blue = np.array([100, 150, 0])  # lower and upper bounds to detect blue color
upper_blue = np.array([120, 255, 255])

lower_green = np.array([65, 60, 60])  # lower and upper bounds to detect green color
upper_green = np.array([80, 255, 255])

def set_channel(index):
    # from select_channel
    channel_info = camera_adapter_info.get(index)
    print("****channel_info set to camera " + index + "****")
    if channel_info == None:
        print("Can't get this info")
    gpio_sta = channel_info["gpio_sta"] # gpio write
    print("****gpio_sta set to channel_info value****")
    GPIO.output(4, gpio_sta[0])
    GPIO.output(17, gpio_sta[1])
    print("****GPIO output pin set****")

def init_i2c(index):  
    # from I2C_init 
    channel_info = camera_adapter_info.get(index)
    print("****channel_info set with camera A****")
    os.system(channel_info["i2c_cmd"]) # i2c write
    print("*****I2C Complete****")

def Detect_Red(cam):   
    start_time = time.time()
    detected_color = None
    while time.time() - start_time < duration:
        frame = cam.capture_array()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_red, upper_red)
        _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for c in cnts:
            min_contour_area = 600
            if cv2.contourArea(c) > min_contour_area:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "DETECT", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                #time.sleep(5)
                detected_color = "red" 
        #if (detected_color == "Green"):
         #   break
        
        print("Detected")
        cv2.imshow("Frame", frame)
        cv2.waitKey(1) 
    cv2.destroyAllWindows()
    return detected_color    
    # return color string into self.Payload_Color

def Detect_Blue(cam): 
    start_time = time.time()
    detected_color = None
    while time.time() - start_time < duration:
        frame = cam.capture_array()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for c in cnts:
            min_contour_area = 600
            if cv2.contourArea(c) > min_contour_area:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "DETECT", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                #time.sleep(5)
                detected_color = "blue" 
        #if (detected_color == "Green"):
         #   break
        
        print("Detected")
        cv2.imshow("Frame", frame)
        cv2.waitKey(1) 
    cv2.destroyAllWindows()
    return detected_color   
    # return color string into self.Payload_Color
    
    
def Detect_Green(cam): 
    start_time = time.time()
    detected_color = None
    while time.time() - start_time < duration:
        frame = cam.capture_array()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_green, upper_green)
        _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for c in cnts:
            min_contour_area = 600
            if cv2.contourArea(c) > min_contour_area:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "DETECT", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                #time.sleep(5)
                detected_color = "green" 
        #if (detected_color == "Green"):
         #   break
        
        print("Detected")
        cv2.imshow("Frame", frame)
        cv2.waitKey(1) 
    cv2.destroyAllWindows()
    return detected_color    
    # return color string into self.Payload_Color
    
    
    
def Main(self):
    for item in {"A", "B"}:
        if item == "A":
            set_channel(item)
            init_i2c(item)
            cam = Picamera2()
            cam.preview_configuration.main.size = (1280, 720)
            cam.preview_configuration.main.format = "RGB888"
            cam.preview_configuration.align()
            cam.configure("preview")
            cam.start()
        else: 
            continue

    while self.Payload_Color == None: 
        self.Payload_Color = Detect_Red()
        self.Payload_Color = Detect_Blue()
        self.Payload_Color = Detect_Green()
        
    
if __name__ == '__main__':
    Main()
    
