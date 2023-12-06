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
pwm_a = GPIO.PWM(ENA,15000)

GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT) 
pwm_b = GPIO.PWM(ENB,15000)

pwm_a.start(0)
pwm_b.start(0) 

GPIO.output(ENA, GPIO.HIGH)
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW) 

GPIO.output(ENB, GPIO.HIGH)
GPIO.output(IN3, GPIO.HIGH)
GPIO.output(IN4, GPIO.LOW) 





pwm_a.ChangeDutyCycle(100)
pwm_b.ChangeDutyCycle(100)


time.sleep(5000)




