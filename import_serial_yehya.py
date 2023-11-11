import serial
import import_RPi as Motors

if __name__ == '__main__':
    global error_int

    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)

    ser.flush()

    while True:
        if ser.in_waiting>0:
            error = ser.readline().decode('utf-8').rstrip() 
            # error = int(error)
            error_int = int(error)
            print("Error in Serial: ", error_int)
            Motors.Main(error_int)

        """             print(type(error))
                    print(error) 
                    print(type(error_int))
                    print(error_int)  """


