import RPi.GPIO as GPIO
import time
# import import_serial_yehya

Kp = 1.5
Ki = 1
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

    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT) 
    pwm_a = GPIO.PWM(ENA,100)
    pwm_a.start(0)
    pwm_b = GPIO.PWM(ENB,100)
    pwm_b.start(0)

    

def Move_forward():
    global ENA, IN1, IN2
    global ENB, IN3, IN4

    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW) 
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW) 
   
   
def calc_PID(error):
 
    global lastError, totalError
    global Kp, Ki, Kd
    P = error  
    totalError = error + totalError  
    I = totalError
    D = error - lastError
    lastError = error

    val_PID = (Kp * P) + (Ki * I) + (Kd * D)

    return val_PID

def calc_DutyCycle(Val_PID):
    global pwm_a, pwm_b

    right_speed = 50 + Val_PID * 5
    left_speed = 50 - Val_PID* 5

    print(left_speed)
    print(right_speed)

    pwm_a.ChangeDutyCycle(left_speed)
    pwm_b.ChangeDutyCycle(right_speed)

def Main(error):
    global pwm_a, pwm_b

    motor_Init()

    print("Error in Motors: ", error)
    val_PID = calc_PID(error)
    calc_DutyCycle(val_PID)
    Move_forward()
    time.sleep(1)
    
    pwm_a.stop(0)
    pwm_b.stop(0) 

    time.sleep(0.01)           




if __name__ == '__main__':
    Main()

