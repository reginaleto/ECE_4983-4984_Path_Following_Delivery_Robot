from picamera2 import Picamera2 
import RPi.GPIO as GPIO
import os
import threading
import time
import cv2
import numpy as np

detected_color = None 

duration = 0.5

lower_red = np.array([126, 188, 47])  # lower and upper bounds to detect red color
upper_red = np.array([179, 255, 255])

lower_blue = np.array([100, 150, 0])  # lower and upper bounds to detect blue color
upper_blue = np.array([120, 255, 255])

lower_green = np.array([65, 60, 60])  # lower and upper bounds to detect green color
upper_green = np.array([80, 255, 255])


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

def set_channel(index): 
        channel_info = camera_adapter_info.get(index)
        if channel_info == None:
            print("Can't get this info")
        gpio_sta = channel_info["gpio_sta"] # gpio write
        GPIO.output(4, gpio_sta[0]) # Camera A - Pin 7
        GPIO.output(17, gpio_sta[1]) # Camera B - Pin 11

def init_i2c(index):
    channel_info = camera_adapter_info.get(index)
    os.system(channel_info["i2c_cmd"]) # i2c write

def detect_green(camera_init, lower_bound, upper_bound):
    global detected_color
    
    frame = camera_init.capture_array()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in cnts:
        min_contour_area = 600
        if cv2.contourArea(c) > min_contour_area:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "DETECT", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            detected_color = "green"
        # cv2.imshow("Detecting....", frame)
        # print("****SHOWING FRAME****")
        # cv2.waitKey(1)
    # cv2.destroyAllWindows() 
    return detected_color


def detect_blue(camera_init, lower_bound, upper_bound):
    global detected_color
    
    frame = camera_init.capture_array()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in cnts:
        min_contour_area = 600
        if cv2.contourArea(c) > min_contour_area:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "DETECT", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            detected_color = "blue"
        # cv2.imshow("Detecting....", frame)
        # print("****SHOWING FRAME****")
        # cv2.waitKey(1)
    # cv2.destroyAllWindows() 
    return detected_color


def detect_red(camera_init, lower_bound, upper_bound):
    global detected_color
    
    frame = camera_init.capture_array()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for c in cnts:
        min_contour_area = 600
        if cv2.contourArea(c) > min_contour_area:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, "DETECT", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
            detected_color = "red"
        # cv2.imshow("Detecting....", frame)
        # print("****SHOWING FRAME****")
        # cv2.waitKey(1)
    # cv2.destroyAllWindows() 
    return detected_color
        

def color_detect(self):
    global camera_init
    global lower_blue, upper_blue
    global lower_green, upper_green
    global lower_red, upper_red
    global duration, detected_color

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    for item in {"A", "B"}: 
        # if item == "B": -- REAL CAMERA PORT 
        if item == "B": # TEST w WIDE 
            set_channel(item)
            init_i2c(item)
            camera_init = Picamera2()
            camera_init.configure(camera_init.create_still_configuration(main={"size": (1280, 720),"format": "RGB888"},buffer_count=2)) 
            camera_init.start()
            camera_init.set_controls({"AeEnable":False,"ExposureTime":30000,"AnalogueGain":6})
            time.sleep(2)
            camera_init.capture_array("main",wait=True)
            time.sleep(0.1)
            
            start_time = time.time()
            while time.time() - start_time < duration:
                while self.Payload_Color == None: 
                    self.Payload_Color = detect_green(camera_init, lower_green, upper_green)
                    self.Payload_Color = detect_red(camera_init, lower_red, upper_red)
                    self.Payload_Color = detect_blue(camera_init, lower_blue, upper_blue)
                """ if self.Payload_Color == None:
                    self.Payload_Color = detect_red(camera_init, lower_red, upper_red)
                    self.Payload_Color = detect_blue(camera_init, lower_blue, upper_blue)
                    self.Payload_Color = detect_green(camera_init, lower_green, upper_green)
                else:
                    break """

            print("Color Detected: ", self.Payload_Color)

if __name__ == '__main__':
    color_detect()