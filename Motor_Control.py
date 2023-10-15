import RPi.GPIO as GPIO

# may need to adjust for position and pins 
ENA = 11
IN1 = 13
IN2 = 15

ENB = 19
IN3 = 21
IN4 = 23

def Motor_Init(): 
    # enable GPIO
    GPIO.setMode(GPIO.BOARD)
    
    # set each used pin on L298N as output
    # left motor
    GPIO.setup(ENA, GPIO.OUT)
    GPIO.setup(IN1, GPIO.OUT)
    GPIO.setup(IN2, GPIO.OUT)
    
    # right motor
    GPIO.setup(ENB, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT)

def Left_Motor(): 
    # move left motor (clockwise I think)
    GPIO.output(ENA, GPIO.HIGH) # speed pin
    GPIO.output(IN1, GPIO.HIGH) # direction pins
    GPIO.output(IN2, GPIO.LOW)
    
    # I think to move forward, one needs to move clockwise and the other counterclockwise
    # speaking from Excursion #2
    
def Right_Motor():
    # move right motor (clockwise I think)
    GPIO.output(ENB, GPIO.HIGH) # speed pin
    GPIO.output(IN3, GPIO.HIGH) # direction pins
    GPIO.output(IN4, GPIO.LOW)
    
def Stop_Movement():
    # set both speed pins to low
    GPIO.output(ENA, GPIO.LOW)
    GPIO.output(ENB, GPIO.LOW)
    
    
def Reverse_Movement():
    # reverse left motor
    GPIO.output(ENA, GPIO.HIGH) # keep moving
    GPIO.output(IN1, GPIO.LOW) # reverse direction
    GPIO.output(IN2, GPIO.HIGH)
    
    # reverse right motor
    GPIO.output(ENB, GPIO.HIGH) # keep moving
    GPIO.output(IN3, GPIO.LOW) # reverse direction
    GPIO.output(IN4, GPIO.HIGH)
    
def Keep_Straight():
# def Keep_Straight()
    # move both motors as defined at the same time 
    
    # may have to put in WHILE loop
   # while(1): 
   # while not Stop_Movement():
   # maybe take in Argument 
   # while input != 1:
    Left_Motor()
    Right_Motor()
    # Stop_Movement()
    
def Main(self):


if __name__ == '__main__':
    Main()
    
        