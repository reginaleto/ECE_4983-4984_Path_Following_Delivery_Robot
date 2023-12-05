import RPi.GPIO as GPIO
import time


# left
ENA = 13
IN1 = 20
IN2 = 21

# right
ENB = 12
IN3 = 19
IN4 = 26

pwm_a = None # left
pwm_b = None # right


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

GPIO.output(ENA, GPIO.HIGH)
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.HIGH) 

GPIO.output(ENB, GPIO.HIGH)
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW) 



time.sleep(5)

pwm_a.ChangeDutyCycle(90)
pwm_b.ChangeDutyCycle(90)




