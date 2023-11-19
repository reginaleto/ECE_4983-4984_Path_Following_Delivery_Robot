import serial
import import_RPi as Motors

if __name__ == '__main__':
    global error_int

    ser = serial.Serial('/dev/ttyACM0',9600, timeout=1)

    ser.flush()

    # Motors.motor_Init()

    while True:
        if ser.in_waiting>0:
            #ser.flushInput()
            error = ser.readline().decode('utf-8').rstrip() 
            if error:
                error_int = int(error)
                print("Received Error from Arduino: ", error_int)
            else:
                print("Corrupt MEssage")
            """ error_int = int(error)
            #error_int = error
            print("Error in Serial: ", error_int)
            # Motors.Main(error_int) """



