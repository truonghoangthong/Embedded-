from machine import Pin, PWM
from utime import sleep

# Servo pin numbers
servoOnePin = 7
servoTwoPin = 8
servoThreePin = 9
servoFourPin = 20

# Initialize servos
servoOne = PWM(Pin(servoOnePin))
servoTwo = PWM(Pin(servoTwoPin))
servoThree = PWM(Pin(servoThreePin))
servoFour = PWM(Pin(servoFourPin))

# Set PWM frequency to 50 Hz for all servos (20ms period)
servoOne.freq(50)
servoTwo.freq(50)
servoThree.freq(50)
servoFour.freq(50)

# Adjusted pulse width values in nanoseconds for testing
deg0 = 600000    # 0.6 ms pulse for 0 degrees
deg90 = 60000  # 1.5 ms pulse for 90 degrees
deg180 = 2400000 # 2.4 ms pulse for 180 degrees

# Function to set a servo angle
def set_servo_angle(servo, angle_ns):
    servo.duty_ns(angle_ns)

# Testing servo movement
while True:
    set_servo_angle(servoTwo, deg90)
    sleep (5)
 
