import RPi.GPIO as GPIO
import time
# import import_serial_yehya
import serial 

Kp = 1.5
Ki = 0.5
Kd = 0.5

# left
ENA = 13
IN1 = 21
IN2 = 20

# right
ENB = 12
IN3 = 19
IN4 = 26

lastError = 0
totalError = 0

pwm_a = None # left
pwm_b = None # right


def motor_Init():
    global pwm_a, pwm_b
    global ENA, IN1, IN2
    global ENB, IN3, IN4

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    pwm_a = GPIO.PWM(ENA,100)
    pwm_a.start(0)

    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT) 
    pwm_b = GPIO.PWM(ENB,100)
    pwm_b.start(0) 

def Move_forward():
    global ENA, IN1, IN2
    global ENB, IN3, IN4

    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH) 
    pwm_a.ChangeDutyCycle(30)

    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW) 
    pwm_b.ChangeDutyCycle(30)

    time.sleep(1.75)
    Stop()

def Turn_Left():
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW) 

    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    #time.sleep(1)
    #Stop()

    pwm_a.ChangeDutyCycle(10)
    pwm_b.ChangeDutyCycle() 


def Turn_Right():
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH) 

    GPIO.output(ENB, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

    pwm_a.ChangeDutyCycle(35)
    pwm_b.ChangeDutyCycle(0) 

def Stop():
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW) 

    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)
   
def calc_PID(error):
    print("Error in calc_PID: ", error)
 
    global lastError, totalError
    global Kp, Ki, Kd
    P = int(error)  
    totalError = int(error) + totalError  
    I = totalError
    D = int(error) - lastError
    lastError = int(error)

    val_PID = (Kp * P) + (Ki * I) + (Kd * D)

    print("Val_PID: ", val_PID)

    return val_PID

def calc_DutyCycle(Val_PID):
    global pwm_a, pwm_b

    right_speed = 0 
    left_speed = 0

    right_speed = 50 + int(Val_PID) * 2
    left_speed = 50 - int(Val_PID) * 2

    print("Left Speed: ", left_speed)
    print("Right Speed: ", right_speed)

    pwm_a.ChangeDutyCycle(left_speed)
    pwm_b.ChangeDutyCycle(right_speed)


def Line_Following():
    global pwm_a, pwm_b

    motor_Init()
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()
    #error_int = 0
    while True:
        if ser.in_waiting > 0:
            error = int(ser.readline().decode('utf-8').rstrip())
            try:
                error_int = error
                print("\n\nIncoming error value:", error_int)
                #val_PID = calc_PID(error_int)
                #calc_DutyCycle(val_PID)
            except ValueError:
                print("Error value is not an integer:", error)


            if (error_int == 0):
                Move_forward()

            if (error_int == 1):
                Turn_Right()
                time.sleep(0.1)
            if (error_int == 2):
                Turn_Right()
                time.sleep(0.1)
            if (error_int == 4):
                Turn_Right()
                time.sleep(0.1)

            if (error_int == -1):
                Turn_Left()
                time.sleep(0.01)
            if (error_int == -2):
                Turn_Left()
                time.sleep(0.1)
            if (error_int == -4):
                Turn_Left()
                time.sleep(0.1)
            
                
if __name__ == '__main__':
    Line_Following()
