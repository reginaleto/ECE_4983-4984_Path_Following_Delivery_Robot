<!---
HOW TO WRITE a README: 

https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

--->

# Path Following Delivery Robot
## Log of Changes throughout Duration of Project

### **October 4, 2023**
### **Changes by:** Gina

### **Additions/Accomplishments**
* Added scripts for each remaining module 
* Added script for Barcode Generation 
* Started experimenting with GUI for Streaming
    - Experimenting with Button on Streaming GUI to start System
* Added Main() function to all module scripts
* Implemented Change Log to keep track of changes to project
* Set up important notes in README

### **Important Notes**
* Found that RPi.GPIO, Picamera2 libraries can only work on Linux systems


### **October 6, 2023**
### **Changes by:** Gina

### **Additions/Accomplishments**
* Added calls to Main in each file individually
* Completed Streaming.py based on Excursion #2
* Updated Instruction_Decode.py to include init and disable of camera, barcode capture, and barcode decode
* Completed Barcode_Gen.py for basic barcode generation (one at a time, hardcoded)
* Implemented algorithm prototype for instruction assignments based on barcode ID and payload color


### **November 19, 2023**
### **Changes by:** Gina & Yehya
#### Highlights Changes Made between 10/9/2023 and 11/19/2023

### ***Additions/Accomplishments**
* AruCam Multi-Camera Adapter is a success! 
    - I2C implemented to isolate streams from both cameras individually
    - Camera_Adapter_Test.py shows both streams at the same time 
* Color Detection Finished 
    - Camera B (Raspbery Pi Camera Module 3 NoIR -- IMX708) only initialized 
    - Searches for red, blue, and green continuously
    - Returns color detected first/primarily
* Instruction Decode Finished
    - Camera A (Raspberry Pi Camera Module 3 NoIR Wide -- IMX708) only initialized
    - Continuous Focus implemented to fix focal distance issue
    - Takes image of barcode after 4 seconds and saves to external file location
    - Extracts barcode image from location and decodes to extract ID number
    - ID Number passed through Instruction_Algorithm function for further instruction
    - System executes instructions based on 
        (1) ID number decoded
        (2) color of payload
* Payload Manipulation Finished 
    - Linear Actuator moves up and down with respective functions
    - Barcodes 5 and 6 confirmed to move linear acuator accordingly
* Motor Movements Finished 
    - Motors stop and move left and right with respective functions
* Sensor Integration works on individual level

### **Still to Finish**
* Line Following
* Finalize System.py script
* Confirm motors move with barcodes 1, 2, 3, and 4
* Confirm threading method for line following and sensor integration within System.py

## **Important Notes**
* Streaming to be paused until further notice
    - Jesslyn unable to get camera working with Raspberry Pi Zero
    - Camera being used with Raspberry Pi Zero broke
    - Current cameras prioritized for Instruction Decode and Color Detection until we can get another third camera 

