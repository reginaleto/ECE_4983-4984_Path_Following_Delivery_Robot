import Instruction_Decode as Barcode
# import Payload_Manipulation as Forklift
# import Motor_Control as Motors
# import Streaming
# import Sensor_Integration as Input



# class System(Streaming.Streaming_GUI):
class System():
    def __init__(self):
        self.Payload_Color = 'green'
        self.ID = ''
            
        #def Start_System():
    
    def Main(self):
        Barcode.Main(self) # -- to test, but not yet complete
        

System.Main()
    