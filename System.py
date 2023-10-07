import Instruction_Decode as Barcode
import Payload_Manipulation as Forklift
import Motor_Control as Motors
import Streaming
import Sensor_Integration as Input



class System(Streaming.Streaming_GUI):
    def __init__(self):
        self.Payload_Color = 'red'
        self.ID = '1'
        
    #def Start_System():
    
    def Main(): 
        # Barcode.Instruction_Algorithm(self) -- to test, but not yet complete
        
    if __name__ == '__main__':
        Main()
    