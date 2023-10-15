import Instruction_Decode as Barcode
# import Payload_Manipulation as Forklift
# import Motor_Control as Motors
# import Streaming
# import Sensor_Integration as Input



class System():
    def __init__(self, parent):
        super().__init__(parent)
        self.Payload_Color = None
        # initialization 
        self.ID = None
        
        
    #def Start_System():
    
    def Main(self):
        Barcode.Main(self) # -- to test, but not yet complete
        
    if __name__ == '__main__':
        Main()
    