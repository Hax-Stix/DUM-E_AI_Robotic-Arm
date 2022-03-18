from telnetlib import theNULL
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#GPIO Pins For CLAW
#FIXME: is meant to be 07 even if it looks like a mistake it refers to the pin number on the RASPBERRY PI - Just Add '#' (Comment) when/for debug
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
#Claw DC Motor Output
#FIXME: is meant to be 07 even if it looks like a mistake it refers to the pin number on the RASPBERRY PI - Just Add '#' (Comment) when/for debug
Claw_DC_Motor_1 = (7)
Claw_DC_Motor_2 = (11)
#Claw PWM Control
pwm_Claw=GPIO.PWM(15, 100)
pwm_Claw.start(0)

#GPIO Pins For Wrist
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
#Wrist DC Motor Output
Wrist_DC_Motor_1 = (13)
Wrist_DC_Motor_2 = (12)
#Wrist PWM Control
pwm_Wrist=GPIO.PWM(16, 100)
pwm_Wrist.start(0)

#GPIO Pins For Elbow
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
#Elbow DC Motor Output
Elbow_DC_Motor_1 = (18)
Elbow_DC_Motor_2 = (22)
#Elbow PWM Control
pwm_Elbow=GPIO.PWM(23, 100)
pwm_Elbow.start(0)

#GPIO Pins For Shoulder Vertical
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
#Shoulder Vertical DC Motor Output
Shoulder_Vertical_DC_Motor_1 = (24)
Shoulder_Vertical_DC_Motor_2 = (26)
#Shoulder Vertical PWM Control
pwm_Shoulder_Vertical=GPIO.PWM(19, 100)
pwm_Shoulder_Vertical.start(0)

#GPIO Pins for Shoulder Horizontal 
GPIO.setup(21, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
#Shoulder Horizontal DC Motor Output
Shoulder_Horizontal_DC_Motor_1 = (21)
Shoulder_Horizontal_DC_Motor_2 = (37)
#Shoulder Horizontal PWM Control
pwm_Shoulder_Horizontal=GPIO.PWM(40, 100)
pwm_Shoulder_Horizontal.start(0)


#GPIO.setup
GPIO.setup(38, GPIO.OUT)
#Claw LED Output
Claw_LED = (38)

time = 0
speed = 0
motion = ""

def Claw_Open():
    print("DUM-Es Claw Is Opening")
    GPIO.output(Claw_DC_Motor_1, True)
    GPIO.output(Claw_DC_Motor_2, False)
    pwm_Claw.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Claw, True)
    sleep(int(speed))
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_2, False)
    GPIO.output(pwm_Claw, False)
    pwm_Claw.stop()
    print("DUM-E Finished Opening Claw")

def Claw_Close():
    print("DUM-Es Claw Is Closing")
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_2, True)
    pwm_Claw.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Claw, True)
    sleep(int(speed))
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(pwm_Claw, False)
    pwm_Claw.stop()
    print("DUM-E Finished Closing Claw")

def Wrist_Up():
    print("DUM-Es Wrist Is Moving Up")
    GPIO.output(Wrist_DC_Motor_1, True)
    GPIO.output(Wrist_DC_Motor_2, False)
    pwm_Wrist.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Wrist, True)
    sleep(int(speed))
    GPIO.output(Wrist_DC_Motor_1, False)
    GPIO.output(Wrist_DC_Motor_2, False)
    GPIO.output(pwm_Wrist, False)
    pwm_Wrist.stop()
    print("DUM-E Finished Moving Wrist Up")

def Wrist_Down():
    print("DUM-Es Wrist is Moving Down")
    GPIO.output(Wrist_DC_Motor_1, False)
    GPIO.output(Wrist_DC_Motor_2, True)
    pwm_Wrist.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Wrist, True)
    sleep(int(speed))
    GPIO.output(Wrist_DC_Motor_1, False)
    GPIO.output(Wrist_DC_Motor_2, False)
    GPIO.output(pwm_Wrist, False)
    pwm_Wrist.stop()
    print("DUM-E Finished Moving Wrist Down")

def Elbow_Up():
    print("DUM-Es Elbow is moving Up")
    GPIO.output(Elbow_DC_Motor_1, True)
    GPIO.output(Elbow_DC_Motor_2, False)
    pwm_Elbow.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Elbow, True)
    sleep(int(speed))
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, False)
    GPIO.output(pwm_Elbow, False)
    pwm_Elbow.stop()
    print("DUM-E Finished Moving Elbow up")
    
def Elbow_Down():
    print("DUM-Es Elbow Is Moving Down")
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, True)
    pwm_Elbow.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Elbow, True)
    sleep(int(speed))
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, False)
    GPIO.output(pwm_Elbow, False)
    pwm_Elbow.stop()
    print("DUM-E Finished Moving Elbow Down")

def Shoulder_Vertical_Up():
    print("DUM-Es Shoulder_Vertical Is Moving Up")
    GPIO.output(Shoulder_Vertical_DC_Motor_1, True)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    pwm_Shoulder_Vertical.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Shoulder_Vertical, True)
    sleep(int(speed))
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    GPIO.output(pwm_Shoulder_Vertical, False)
    pwm_Shoulder_Vertical.stop()
    print("DUM-E Finished Moving Shoulder_Vertical Up")

def Shoulder_Vertical_Down():
    print("DUM-Es Shoulder_Vertical Is Moving Down")
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, True)
    pwm_Shoulder_Vertical.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Shoulder_Vertical, True)
    sleep(int(speed))
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    GPIO.output(pwm_Shoulder_Vertical, False)
    pwm_Shoulder_Vertical.stop()
    print("DUM-E Finished Moving Down")

def Shoulder_Horizontal_Right():
    print("DUM-Es Shoulder_Horizontal Is Moving Right")
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, True)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
    pwm_Shoulder_Horizontal.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Shoulder_Horizontal, True)
    sleep(int(speed))
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(pwm_Shoulder_Horizontal, False)
    pwm_Shoulder_Horizontal.stop()
    print("DUM-E Finished Moving Shoulder_Horizontal Right")

def Shoulder_Horizontal_Left():
    print("DUM-Es Shoulder_Horizontal Is Moving Left")
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, True)
    pwm_Shoulder_Horizontal.ChangeDutyCycle(int(speed))
    GPIO.output(pwm_Shoulder_Horizontal, True)
    sleep(int(speed))
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
    GPIO.output(pwm_Shoulder_Horizontal, False)
    pwm_Shoulder_Horizontal.stop()
    print("DUM-E Finished Shoulder_Horizontal Moving Left")

def LED_On():
    GPIO.output(Claw_LED, True)

def LED_Off():
    GPIO.output(Claw_LED, False)


while True:
    time = input("Enter Time:")
    speed = input("Enter Speed:")
    print("A. Claw Open\n""B. Claw Close\n""C. Wrist Up\n""D. Wrist Down\n""E. Elbow Up\n""F. Elbow Down\n""G. Shoulder Vertical Up\n""H. Shoulder Vertical Down\n""I. Shoulder Horizontal Left\n""J. Shoulder Horizontal Right\n""Exit")
    motion = input("Enter Motion:")

    if motion == "A" or "a":
        Claw_Open()
        motion = ""

    if motion == "B" or "b":
        Claw_Close()
        motion = ""

    if motion == "C" or "c":
        Wrist_Up()
        motion = ""

    if motion == "D" or "d":
        Wrist_Down()
        motion = ""

    if motion == "E" or "e":
        Elbow_Up()
        motion = ""

    if motion == "F" or "f":
        Elbow_Down()
        motion = ""

    if motion == "G" or "g":
        Shoulder_Vertical_Up()
        motion = ""

    if motion == "H" or "h":
        Shoulder_Vertical_Down()
        motion = ""

    if motion == "I" or "i":
        Shoulder_Horizontal_Left()
        motion = ""

    if motion == "J" or "j":
        Shoulder_Horizontal_Right()
        motion = ""

    if motion == "Exit" or "exit"  or "Ex" or "ex":
        break