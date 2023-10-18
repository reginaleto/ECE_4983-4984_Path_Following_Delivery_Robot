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