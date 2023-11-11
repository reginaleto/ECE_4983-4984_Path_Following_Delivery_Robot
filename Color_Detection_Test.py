from picamera2 import Picamera2 
import RPi.GPIO as GPIO
import os
import threading
import time
import cv2

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
        print("channel selected")

def init_i2c(index):
    channel_info = camera_adapter_info.get(index)
    print("****channel_info set with camera A****")
    os.system(channel_info["i2c_cmd"]) # i2c write
    print("*****I2C Complete****")


def color_detect():
    global camera_init

    for item in {"A", "B"}: 
        # if item == "B": -- REAL CAMERA PORT 
        if item == "A": # TEST w WIDE 
            set_channel(item)
            init_i2c(item)
            camera_init = Picamera2()
            camera_init.preview_configuration.main.size = (1280, 720)
            camera_init.preview_configuration.main.format = "RGB888"
            camera_init.preview_configuration.align()
            camera_init.configure("preview")
            camera_init.start()