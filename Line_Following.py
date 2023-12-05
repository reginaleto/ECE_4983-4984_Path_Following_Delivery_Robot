import RPi.GPIO as GPIO
import serial
import time 

pwm_a = None
pwm_b = None

# left motor
ENA = 13
IN1 = 21
IN2 = 20

# right motor
ENB = 12
IN3 = 19
IN4 = 26



def Motor_Init(): 
    global pwm_a, pwm_b
    global ENA, IN1, IN2
    global ENB, IN3, IN4

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    pwm_a = GPIO.PWM(ENA,100)

    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT) 
    pwm_b = GPIO.PWM(ENB,100)

    pwm_a.start(0)
    pwm_b.start(0) 
 
def Turn_Left(a_duty, b_duty): 
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH) 

    GPIO.output(ENB, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

    pwm_a.ChangeDutyCycle(a_duty)
    pwm_b.ChangeDutyCycle(b_duty) 


def Turn_Right(a_duty, b_duty): 
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW) 

    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

    pwm_a.ChangeDutyCycle(a_duty)
    pwm_b.ChangeDutyCycle(b_duty) 


def Move_Forward(): 
    global ENA, IN1, IN2
    global ENB, IN3, IN4

    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW) 
    
    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

    pwm_a.ChangeDutyCycle(15)
    pwm_b.ChangeDutyCycle(15)

    time.sleep(10)


def Stop(): 
    GPIO.output(ENA, GPIO.HIGH)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW) 

    GPIO.output(ENB, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

    pwm_a.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

def Error_Input(error_val): 

    if error_val != 0: 
        if error_val == -3: 
            Stop()
            time.sleep(0.5) 
            Turn_Right(a, b)
            Move_Forward()
            
        if error_val == -2: 
            Stop()
            time.sleep(0.5) 
            Turn_Right(a, b)
            Move_Forward()

        if error_val == -1: 
            Stop()
            time.sleep(0.5) 
            Turn_Right(a, b)
            Move_Forward()

        if error_val == 1: 
            Stop()
            time.sleep(0.5) 
            Turn_Left(a, b)
            Move_Forward()

        if error_val == 2: 
            Stop()
            time.sleep(0.5) 
            Turn_Left(a, b)
            Move_Forward()

        if error_val == 3: 
            Stop()
            time.sleep(0.5) 
            Turn_Left(a, b)
            Move_Forward()
        
        if error_val == 5: 
            Stop()

    elif error_val == 0: 
        Move_Forward()
    


def Line_Follow(): 
    global pwm_a, pwm_b

    Motor_Init()
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            error = int(ser.readline().decode('utf-8').rstrip())
            try:
                error_int = error
                print("\n\nIncoming error value:", error_int)

                Error_Input(error_int) # 
            except ValueError:
                print("Error value is not an integer:", error)

