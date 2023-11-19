# Is there a way for it to output without exiting the frame? Yes
# 

import cv2
from picamera2 import Picamera2
import numpy as np
import time

cam = Picamera2()
cam.preview_configuration.main.size = (300, 300)
cam.preview_configuration.main.format = "RGB888"
cam.preview_configuration.align()
cam.configure("preview")
cam.start()

lower_red = np.array([126, 188, 47])  # lower and upper bounds to detect red color
upper_red = np.array([179, 255, 255])

lower_blue = np.array([100, 150, 0])  # lower and upper bounds to detect blue color
upper_blue = np.array([120, 255, 255])

lower_green = np.array([65, 60, 60])  # lower and upper bounds to detect green color
upper_green = np.array([80, 255, 255])

def detect_color(cam, lower_bound, upper_bound, duration=60):
    start_time = time.time()
    detected_color = None
    while time.time() - start_time < duration:
        frame = cam.capture_array()
        print("frame: ", frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        print("hsv: ", str(hsv))
        mask = cv2.inRange(hsv, lower_bound, upper_bound)
        print("lower bound: ", lower_bound)
        print("upper_bound: ", upper_bound)
        print("mask: ", mask)
        _, mask1 = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        print("mask1: ", mask1)
        cnts, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        print("cnts: ", cnts)
        for c in cnts:
            min_contour_area = 600
            if cv2.contourArea(c) > min_contour_area:
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, "DETECT", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
                #time.sleep(5)
                detected_color = "Green" 
        #if (detected_color == "Green"):
         #   break
        
        print("Detected: ", detected_color)
        cv2.imshow("Frame", frame)
        cv2.waitKey(1) 
    cv2.destroyAllWindows()
    return detected_color

def main():
    color1 = detect_color(cam, lower_green, upper_green)
    print("Detected Color:", color1)

if __name__ == "__main__":
    main()
