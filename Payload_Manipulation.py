import RPi.GPIO as GPIO
import time

# Define pin numbers for Raspberry PI GPIO
ENA_PIN = 19
IN1_PIN = 5
IN2_PIN = 6
#LEFT_LIMIT_SWITCH_PIN = #?
#RIGHT_LIMIT_SWITCH_PIN = #?


def Motor_init():
  GPIO.setmode(GPIO.BCM) # change to BCM -- find another pin for IN1 b/c 11 is used by cameras
  # GPIO.setwarnings(False)

  # Initialize pins on the Motor Driver board for output
  #GPIO.setup(ENA_PIN, GPIO.OUT)
  GPIO.setup(IN1_PIN, GPIO.OUT)
  GPIO.setup(IN2_PIN, GPIO.OUT)

 
def Bring_Up():
   
   # Start upward movement for Linear Actuator
   #GPIO.output(ENA_PIN, GPIO.HIGH)

   GPIO.output(IN1_PIN, GPIO.LOW)
   GPIO.output(IN2_PIN, GPIO.HIGH)

   # Run the motor for 10 seconds
   time.sleep(5)

   GPIO.output(IN1_PIN, GPIO.LOW)

   #Stop the motor
   #GPIO.output(ENA_PIN, GPIO.LOW)


def Bring_Down():
   
   #Start downward movement for Linear Actuator
   #GPIO.output(ENA_PIN, GPIO.HIGH)
   GPIO.output(IN1_PIN, GPIO.HIGH)
   GPIO.output(IN2_PIN, GPIO.LOW)

   # Run the motor for 10 seconds
   time.sleep(5)

   GPIO.output(IN1_PIN, GPIO.LOW)

   #Stop the motor
   #GPIO.output(ENA_PIN, GPIO.LOW)

   print("down")



""" def limit_switch_data_read():
   # Configure GPIO pins for input
   GPIO.setup(LEFT_LIMIT_SWITCH_PIN, GPIO.IN)
   GPIO.setup(RIGHT_LIMIT_SWITCH_PIN, GPIO.IN)

   while True:
      left_limit_switch_state = GPIO.input(LEFT_LIMIT_SWITCH_PIN)
      right_limit_switch_state = GPIO.input(RIGHT_LIMIT_SWITCH_PIN)


      # Check for intersection between payload and forklift
      if left_limit_switch_state == 1 or right_limit_switch_state == 1:
         return left_limit_switch_state, right_limit_switch_state
     
 """

def Main():
    try:
       Motor_init()

       # Test for bring_up and bring_down functions       
       #time.sleep(20)
       Bring_Down()


       """ # Test the limit_switch_data functions
       left_state, right_state = limit_switch_data_read()
       print("Left Limit Switch State:", left_state)
       print("Right Limit Switch State:", right_state) """

    except KeyboardInterrupt:
       GPIO.cleanup()
       print("dont work")


if __name__ == '__main__':
    Main()
  




""" Next Step
1. Calculate how much time it takes to go to different positions along the y-axis
2. 
"""