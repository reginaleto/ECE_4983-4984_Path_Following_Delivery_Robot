from picamera2 import Picamera2 
import RPi.GPIO as GPIO
import os
import threading
import time
import cv2
from libcamera import controls

from PyQt5.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QApplication, QWidget 
from picamera2 import Picamera2
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import QThread,Qt

width = 320
height = 240

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
 
class WorkThread(threading.Thread):

    def __init__(self):
        super(WorkThread,self).__init__()
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.OUT)
        GPIO.setup(17, GPIO.OUT)
        print("GPIO set")

    def select_channel(self,index):
        channel_info = camera_adapter_info.get(index)
        if channel_info == None:
            print("Can't get this info")
        gpio_sta = channel_info["gpio_sta"] # gpio write
        GPIO.output(4, gpio_sta[0])
        GPIO.output(17, gpio_sta[1])
        print("channel selected")

    def init_i2c(self,index):
        channel_info = camera_adapter_info.get(index)
        os.system(channel_info["i2c_cmd"]) # i2c write
        print("I2C initialized")

    def run(self):
        global camera_init
        flag = False
        for item in {"A","B"}:
            try:
                self.select_channel(item)
                print("current index: " + item)
                self.init_i2c(item)
                time.sleep(0.5) 
                # if flag == False:
                #     flag = True
                # else :
                camera_init.close()
                    # time.sleep(0.5) 
                print("init1 "+ item)
                camera_init = Picamera2()
                # print(picam2.set_controls())
                camera_init.configure(camera_init.create_still_configuration(main={"size": (320, 240),"format": "BGR888"},buffer_count=2)) 
                camera_init.start()
                camera_init.set_controls({"AfMode": controls.AfModeEnum.Continuous,"AeEnable":False,"ExposureTime":30000,"AnalogueGain":6})
                time.sleep(2)
                camera_init.capture_array("main",wait=True)
                time.sleep(0.1)
            except Exception as e:
                print("except: "+str(e))

        while True:
            for item in {"A","B"}:
                self.select_channel(item)
                time.sleep(0.02)
                try:
                    buf = camera_init.capture_array("main",wait=True)
                    buf = camera_init.capture_array("main",wait=True)
                    
                    cvimg = QImage(buf, width, height,QImage.Format_RGB888)
                    pixmap = QPixmap(cvimg)
                    if item == 'A':
                        image_label.setPixmap(pixmap)
                    elif item == 'B':
                        image_label2.setPixmap(pixmap)
                except Exception as e:
                    print("capture_buffer: "+ str(e))

app = QApplication([])

window = QWidget()
layout_v = QVBoxLayout()
image_label = QLabel()
image_label2 = QLabel()
layout_h = QHBoxLayout()

work = WorkThread()

camera_init = Picamera2()


if __name__ == '__main__':
    image_label.setFixedSize(320, 240)
    image_label2.setFixedSize(320, 240)

    layout_h.addWidget(image_label)    
    layout_h.addWidget(image_label2)
    layout_v.addLayout(layout_h)
    window.setLayout(layout_v)

    work.start()

    window.show()
    app.exec()
    work.quit()
    camera_init.close()