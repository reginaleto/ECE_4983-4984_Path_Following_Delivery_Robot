import RPi.GPIO as GPIO
from time import sleep 

Kp = 0
Kd = 0
Ki = 0

lastError = 0
totalError = 0


def Calc_PID(error):

    P = error
    
    totalError += error
    I = totalError * Ki
    D = error - lastError
    lastError = error

    dutyCycle = (Kp*P) + (Ki*I) + (Kd*D)
    return dutyCycle


def Motor_Init():

    GPIO.setmode(GPIO.BCM)

    ENA = 13
    IN1 = 21
    IN2 = 20

    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    pwm = GPIO.PWM(ENA,0)
    pwm.start(0)

def Move_Forward(dutyCycle):
    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.HIGH)
    pwm.ChangeDutyCycle(dutyCycle) 
    


""" 
def Motor_Init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    

def Move():
    GPIO.output(20, GPIO.HIGH) 
    GPIO.output(21, GPIO.LOW) 


def Main():
    try:
       Motor_Init()

       Move()

    except KeyboardInterrupt:
       GPIO.cleanup()
       print("dont work")
 

if __name__ == '__main__':
    Main()"""