import picamera2
import cv2


def Detect_Red():   
    
    # return color string into self.Payload_Color

def Detect_Blue(): 
    
    # return color string into self.Payload_Color
    
    
def Detect_Green(): 
    
    # return color string into self.Payload_Color
    
    
    
def Main(self):
    while self.Payload_Color == None: 
        self.Payload_Color = Detect_Red()
        self.Payload_Color = Detect_Blue()
        self.Payload_Color = Detect_Green()
        
    
if __name__ == '__main__':
    Main()
    
