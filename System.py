import Instruction_Decode as Barcode
import Payload_Manipulation as Forklift
import Motor_Control as Motors
import Streaming
import Sensor_Integration as Input



class System(Streaming.Streaming_GUI):
    def __init__(self):
        self.Payload_Color = ''
        
    def Start_System()