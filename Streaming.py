# import picamera2 -- only works on Linux
import wx
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder, Quality
import time
import cv2

def Stream(): 
    
    stream = Picamera2()
    config = stream.create_preview_configuration()
    stream.configure(config)
    encoder = H264Encoder(bitrate=10000000)
    stream.start_recording(encoder, '/home/ginaleto/ECE_4983-4984_Path_Following_Delivery_Robot/System_Stream.h264')
    time.sleep(1) # set to however long we want to run the entire system
    stream.stop_recording()

    # need to figure out a way to get stream until keypress


def Main(): 
    Stream()


if __name__ == '__main__':
    Main()




