import Instruction_Decode as Barcode
import camera_adapter_test as camera_test
# import Payload_Detection as Color_Detect
# import Payload_Manipulation as Forklift
# import Motor_Control as Motors
# import Streaming
# import Sensor_Integration as Input


class System(): 
    def __init__(self):
        self.Payload_Color = "Blue"
        self.Previous_Color = None
        self.ID = None
        self.camera_adapter_info = {  
        # A is camera for barcodes (wide)
        "A" : {   
            "i2c_cmd":"i2cset -y 1 0x70 0x00 0x01",
            "gpio_sta":[0,0],
        }, 
        # B is camera for color detection (regular)
        "B" : {
            "i2c_cmd":"i2cset -y 1 0x70 0x00 0x02",
            "gpio_sta":[1,0],
        }
    }

    def Main(self):
        # Color_Detect.Main(self)
        # barcode_thread = Barcode.WorkThread()
        Barcode.Main(self)

        #camera = camera_test.WorkThread()
        #camera.start()

        

system_test = System()
system_test.Main()
    