import Instruction_Decode as Barcode
import Payload_Detection as Color_Detect
# import Payload_Manipulation as Forklift
# import Motor_Control as Motors
# import Streaming
# import Sensor_Integration as Input


class System(): 
    def __init__(self):
        self.Payload_Color = None
        self.Previous_Color = None
        self.ID = None

    def Main(self):
        Color_Detect.Main(self)
       # Barcode.Main(self)

system_test = System()
system_test.Main()
    