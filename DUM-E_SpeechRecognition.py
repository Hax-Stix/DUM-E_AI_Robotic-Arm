import speech_recognition as sr
#FIXME: Possible Problem Here wit RPi.GPIO
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
#Claw Position
Claw_Pos = int(0)

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
#Wrist Position
Wrist_Pos = int(0)

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
#Elbow Position
Elbow_Pos = int(0)

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
#Shoulder Vertical Position
Shoulder_Vertical_Pos = int(0)

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
#Shoulder Horizontal Position
Shoulder_Horizontal_Pos = int(0)


#GPIO.setup
GPIO.setup(38, GPIO.OUT)
#Claw LED Output
Claw_LED = (38)



r = sr.Recognizer()
mic = sr.Microphone()

#Command To Fully Open Claw
def Claw_Fully_Open():
    if Claw_Pos <= 9:
        print("DUM-Es Claw Is Fully Opening")
        GPIO.output(Claw_DC_Motor_1, True)
        GPIO.output(Claw_DC_Motor_2, False)
        pwm_Claw.ChangeDutyCycle(50)
        GPIO.output(pwm_Claw, True)
        sleep(abs(Claw_Pos-(10*1)))
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_2, False)
        GPIO.output(pwm_Claw, False)
        pwm_Claw.stop()
        print("DUM-E Finished Fully Opening Claw")
        Claw_Pos = 10
    else:
        print("DUM-Es Claw Is Already Fully Opened")

#Command To Open Claw
def Claw_Open():
    if Claw_Pos <= 9:
        print("DUM-Es Claw Is Opening")
        GPIO.output(Claw_DC_Motor_1, True)
        GPIO.output(Claw_DC_Motor_2, False)
        pwm_Claw.ChangeDutyCycle(50)
        GPIO.output(pwm_Claw, True)
        sleep(1)
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_2, False)
        GPIO.output(pwm_Claw, False)
        pwm_Claw.stop()
        print("DUM-E Finished Opening Claw")
        Claw_Pos = Claw_Pos + 1
    else:
        print("DUM-E Cannot Open Claw Any Further")

#Command To Move Claw To Middle Location
def Claw_Middle():
    if Claw_Pos == 0:
        print("DUM-Es Claw Is Already Located In The Middle")
    elif Claw_Pos > 0:
        print("DUM-Es Claw Is Opening Towards Middle")
        GPIO.output(Claw_DC_Motor_1, True)
        GPIO.output(Claw_DC_Motor_2, False)
        pwm_Claw.ChangeDutyCycle(50)
        GPIO.output(pwm_Claw, True)
        sleep(abs(Claw_Pos-(0*1)))
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_2, False)
        GPIO.output(pwm_Claw, False)
        pwm_Claw.stop()
        print("DUM-E Finished Opening Claw To Middle")
        Claw_Pos = 0
    elif Claw_Pos < 0:
        print("DUM-Es Claw Is Closing Towards Middle")
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_2, True)
        pwm_Claw.ChangeDutyCycle(50)
        GPIO.output(pwm_Claw, True)
        sleep(abs(Claw_Pos-(0*1)))
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(pwm_Claw, False)
        pwm_Claw.stop()
        print("DUM-E Finished Closing Claw To Middle")
        Claw_Pos = 0

#Command To Close Claw
def Claw_Close():
    if Claw_Pos >= -9:
        print("DUM-Es Claw Is Closing")
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_2, True)
        pwm_Claw.ChangeDutyCycle(50)
        GPIO.output(pwm_Claw, True)
        sleep(1)
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(pwm_Claw, False)
        pwm_Claw.stop()
        print("DUM-E Finished Closing Claw")
        Claw_Pos = Claw_Pos - 1
    else:
        print("DUM-E Cannot Close Claw Any Further")

#Command to Fully Close Claw
def Claw_Fully_Close():
    if Claw_Pos >= -9:
        print("DUM-Es Claw Is Fully Closing")
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_2, True)
        pwm_Claw.ChangeDutyCycle(50)
        GPIO.output(pwm_Claw, True)
        sleep(abs(Claw_Pos-(-10*1)))
        GPIO.output(Claw_DC_Motor_1, False)
        GPIO.output(Claw_DC_Motor_2, False)
        GPIO.output(pwm_Claw, False)
        pwm_Claw.stop()
        print("DUM-E Finished Fully Closing Claw")
        Claw_Pos = -10
    else:
        print("DUM-Es Claw Is Already Fully Closed")

#Command To Move Wrist Up
def Wrist_Up():
    if Wrist_Pos <= 19:
        print("DUM-Es Wrist Is Moving Up")
        GPIO.output(Wrist_DC_Motor_1, True)
        GPIO.output(Wrist_DC_Motor_2, False)
        pwm_Wrist.ChangeDutyCycle(50)
        GPIO.output(pwm_Wrist, True)
        sleep(1)
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, False)
        GPIO.output(pwm_Wrist, False)
        pwm_Wrist.stop()
        print("DUM-E Finished Moving Wrist Up")
        Wrist_Pos = Wrist_Pos + 1
    else:
        print("DUM-Es Wrist Cannot Move Up Any Further")

#Command To Move Wrist Fully Up
def Wrist_Fully_Up():
    if Wrist_Pos <= 19:
        print("DUM-Es Wrist Is Moving Up")
        GPIO.output(Wrist_DC_Motor_1, True)
        GPIO.output(Wrist_DC_Motor_2, False)
        pwm_Wrist.ChangeDutyCycle(50)
        GPIO.output(pwm_Wrist, True)
        sleep(abs(Wrist_Pos-(20*1)))
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, False)
        GPIO.output(pwm_Wrist, False)
        pwm_Wrist.stop()
        print("DUM-E Finished Moving Wrist Up")
        Wrist_Pos = 20
    else:
        print("DUM-Es Wrist Is Already Fully Up")

def Wrist_Middle():
    if Wrist_Pos > 0:
        print("DUM-Es Wrist Is Moving Upwards Towards Middle")
        GPIO.output(Wrist_DC_Motor_1, True)
        GPIO.output(Wrist_DC_Motor_2, False)
        pwm_Wrist.ChangeDutyCycle(50)
        GPIO.output(pwm_Wrist, True)
        sleep(abs(Wrist_Pos-(0*1)))
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, False)
        GPIO.output(pwm_Wrist, False)
        pwm_Wrist.stop()
        print("DUM-E Finished Moving Wrist Up To Middle")
        Wrist_Pos = 0
    elif Wrist_Pos < 0:
        print("DUM-Es Wrist Is Moving Downwards Towards Middle")
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, True)
        pwm_Wrist.ChangeDutyCycle(50)
        GPIO.output(pwm_Wrist, True)
        sleep(abs(Wrist_Pos-(0*1)))
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, False)
        GPIO.output(pwm_Wrist, False)
        pwm_Wrist.stop()
        print("DUM-E Finished Moving Wrist Down To Middle")
        Wrist_Pos = 0
    else:
        print("DUM-Es Wrist Is Already Located In The Middle")

def Wrist_Fully_Down():
    if Wrist_Pos >= -19:
        print("DUM-Es Wrist Is Moving Fully Down")
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, True)
        pwm_Wrist.ChangeDutyCycle(50)
        GPIO.output(pwm_Wrist, True)
        sleep(abs(Wrist_Pos-(-20*1)))
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, False)
        GPIO.output(pwm_Wrist, False)
        pwm_Wrist.stop()
        print("DUM-E Finished Moving Fully Wrist Up")
        Wrist_Pos = -20
    else:
        print("DUM-Es Claw Is Already Located In The Middle")


def Wrist_Down():
    if Wrist_Pos >= -19:
        print("DUM-Es Wrist is Moving Down")
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, True)
        pwm_Wrist.ChangeDutyCycle(50)
        GPIO.output(pwm_Wrist, True)
        sleep(1)
        GPIO.output(Wrist_DC_Motor_1, False)
        GPIO.output(Wrist_DC_Motor_2, False)
        GPIO.output(pwm_Wrist, False)
        pwm_Wrist.stop()
        print("DUM-E Finished Moving Wrist Down")
        Wrist_Pos = Wrist_Pos - 1
    else:
        print("DUM-Es Wrist Is Already Fully Down")


def Elbow_Up():
    if Elbow_Pos <= 19:
        print("DUM-Es Elbow is moving Up")
        GPIO.output(Elbow_DC_Motor_1, True)
        GPIO.output(Elbow_DC_Motor_2, False)
        pwm_Elbow.ChangeDutyCycle(50)
        GPIO.output(pwm_Elbow, True)
        sleep(1)
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, False)
        GPIO.output(pwm_Elbow, False)
        pwm_Elbow.stop()
        print("DUM-E Finished Moving Elbow up")
        Elbow_Pos = Elbow_Pos + 1
    else:
        print("DUM-Es Elbow Is Fully Up")

def Elbow_Fully_Up():
    if Elbow_Pos <= 19:
        print("DUM-Es Elbow Is Fully Moving Up")
        GPIO.output(Elbow_DC_Motor_1, True)
        GPIO.output(Elbow_DC_Motor_2, False)
        pwm_Elbow.ChangeDutyCycle(50)
        GPIO.output(pwm_Elbow, True)
        sleep(abs(Elbow_Pos-(20*1)))
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, False)
        GPIO.output(pwm_Elbow, False)
        pwm_Elbow.stop()
        print("DUM-E Finished Moving Elbow Fully Up")
        Elbow_Pos = 20
    else:
        print("DUM-Es Elbow Is Already Fully Up")


def Elbow_Middle():
    if Elbow_Pos > 0:
        print("DUM-Es Elbow Is Moving Upwards Towards Middle")
        GPIO.output(Elbow_DC_Motor_1, True)
        GPIO.output(Elbow_DC_Motor_2, False)
        pwm_Elbow.ChangeDutyCycle(50)
        GPIO.output(pwm_Elbow, True)
        sleep(abs(Elbow_Pos-(0*1)))
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, False)
        GPIO.output(pwm_Elbow, False)
        pwm_Elbow.stop()
        print("DUM-E Finished Moving Elbow Up To Middle")
        Elbow_Pos = 0
    elif Elbow_Pos < 0:
        print("DUM-Es Elbow Is Moving Downwards Towards Middle")
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, True)
        pwm_Elbow.ChangeDutyCycle(50)
        GPIO.output(pwm_Elbow, True)
        sleep(abs(Elbow_Pos-(0*1)))
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, False)
        GPIO.output(pwm_Elbow, False)
        pwm_Elbow.stop()
        print("DUM-E Finished Moving Elbow Down To Middle")
        Elbow_Pos = 0
    else:
        print("DUM-Es Elbow Is Already Located In The Middle")

def Elbow_Down():
    if Elbow_Pos >= -19:
        print("DUM-Es Elbow Is Moving Down")
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, True)
        pwm_Elbow.ChangeDutyCycle(50)
        GPIO.output(pwm_Elbow, True)
        sleep(1)
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, False)
        GPIO.output(pwm_Elbow, False)
        pwm_Elbow.stop()
        print("DUM-E Finished Moving Elbow Down")
        Elbow_Pos = Elbow_Pos - 1
    else:
        print("DUM-Es Elbow Is Fully Down")

def Elbow_Fully_Down():
    if Elbow_Pos >= -19:
        print("DUM-Es Elbow Is Moving Fully Down")
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, True)
        pwm_Elbow.ChangeDutyCycle(50)
        GPIO.output(pwm_Elbow, True)
        sleep(abs(Elbow_Pos-(-20*1)))
        GPIO.output(Elbow_DC_Motor_1, False)
        GPIO.output(Elbow_DC_Motor_2, False)
        GPIO.output(pwm_Elbow, False)
        pwm_Elbow.stop()
        print("DUM-E Finished Moving Elbow Fully Down")
        Elbow_Pos = -20
    else:
        print("DUM-Es Elbow Is Fully Down")


def Shoulder_Vertical_Up():
    if Shoulder_Vertical_Pos <= 19:
        print("DUM-Es Shoulder_Vertical Is Moving Up")
        GPIO.output(Shoulder_Vertical_DC_Motor_1, True)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        pwm_Shoulder_Vertical.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Vertical, True)
        sleep(1)
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Vertical, False)
        pwm_Shoulder_Vertical.stop()
        print("DUM-E Finished Moving Shoulder_Vertical Up")
        Shoulder_Vertical_Pos = Shoulder_Vertical_Pos + 1
    else:
        print("DUM-Es Shoulder Vertical Is Fully Up")

def Shoulder_Vertical_Fully_Up():
    if Shoulder_Vertical_Pos <= 19:
        print("DUM-Es Shoulder_Vertical Is Moving Fully Up")
        GPIO.output(Shoulder_Vertical_DC_Motor_1, True)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        pwm_Shoulder_Vertical.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Vertical, True)
        sleep(abs(Shoulder_Vertical_Pos-(20*1)))
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Vertical, False)
        pwm_Shoulder_Vertical.stop()
        print("DUM-E Finished Moving Shoulder_Vertical Fully Up")
        Shoulder_Vertical_Pos = 20
    else:
        print("DUM-Es Shoulder Vertical Already Is Fully Up")

def Shoulder_Vertical_Middle():
    if Shoulder_Vertical_Pos > 0:
        print("DUM-Es Shoulder_Vertical Is Moving Upwards Towards Middle")
        GPIO.output(Shoulder_Vertical_DC_Motor_1, True)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        pwm_Shoulder_Vertical.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Vertical, True)
        sleep(abs(Shoulder_Vertical_Pos-(0*1)))
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Vertical, False)
        pwm_Shoulder_Vertical.stop()
        print("DUM-E Finished Moving Shoulder_Vertical Up To Middle")
        Shoulder_Vertical_Pos = 0
    elif Shoulder_Vertical_Pos < 0:
        print("DUM-Es Shoulder_Vertical Is Moving Downwards Towards Middle")
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, True)
        pwm_Shoulder_Vertical.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Vertical, True)
        sleep(abs(Shoulder_Vertical_Pos-(0*1)))
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Vertical, False)
        pwm_Shoulder_Vertical.stop()
        print("DUM-E Finished Moving Shoulder_Vertical Down To Middle")
        Shoulder_Vertical_Pos = 0
    else:
        print("DUM-Es Shoulder_Vertical Is Already Located In The Middle")

def Shoulder_Vertical_Fully_Down():
    if Shoulder_Vertical_Pos >= -19:
        print("DUM-Es Shoulder_Vertical Is Moving Fully Down")
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, True)
        pwm_Shoulder_Vertical.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Vertical, True)
        sleep(abs(Shoulder_Vertical_Pos-(-20*1)))
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Vertical, False)
        pwm_Shoulder_Vertical.stop()
        print("DUM-E Finished Moving Fully Down")
        Shoulder_Vertical_Pos = -20
    else:
        print("DUM-Es Shoulder Vertical is Already Fully Down")

def Shoulder_Vertical_Down():
    if Shoulder_Vertical_Pos >= -19:
        print("DUM-Es Shoulder_Vertical Is Moving Down")
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, True)
        pwm_Shoulder_Vertical.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Vertical, True)
        sleep(1)
        GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
        GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Vertical, False)
        pwm_Shoulder_Vertical.stop()
        print("DUM-E Finished Moving Down")
        Shoulder_Vertical_Pos = Shoulder_Vertical_Pos - 1
    else:
        print("DUM-Es Shoulder Vertical is Fully Down")


def Shoulder_Horizontal_Right():
    if Shoulder_Horizontal_Pos <= 29:
        print("DUM-Es Shoulder_Horizontal Is Moving Right")
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, True)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
        pwm_Shoulder_Horizontal.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Horizontal, True)
        sleep(1)
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(pwm_Shoulder_Horizontal, False)
        pwm_Shoulder_Horizontal.stop()
        print("DUM-E Finished Moving Shoulder_Horizontal Right")
        Shoulder_Horizontal_Pos = Shoulder_Horizontal_Pos + 1
    else:
        print("DUM-E Shoulder_Horizontal Is Right")

def Shoulder_Horizontal_Fully_Right():
    if Shoulder_Horizontal_Pos <= 29:
        print("DUM-Es Shoulder_Horizontal Is Moving Fully Right")
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, True)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
        pwm_Shoulder_Horizontal.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Horizontal, True)
        sleep(abs(Shoulder_Horizontal_Pos-(30*1)))
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(pwm_Shoulder_Horizontal, False)
        pwm_Shoulder_Horizontal.stop()
        print("DUM-E Finished Moving Shoulder_Horizontal Fully Right")
        Shoulder_Horizontal_Pos = 30
    else:
        print("DUM-E Shoulder_Horizontal Is Already Fully Right")

def Shoulder_Horizontal_Middle():
    if Shoulder_Horizontal_Pos > 0:
        print("DUM-Es Shoulder_Horizontal Is Moving Right Towards Middle")
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, True)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
        pwm_Shoulder_Horizontal.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Horizontal, True)
        sleep(abs(Shoulder_Horizontal_Pos-(0*1)))
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Horizontal, False)
        pwm_Shoulder_Horizontal.stop()
        print("DUM-E Finished Moving Shoulder_Horizontal Right To Middle")
        Shoulder_Horizontal_Pos = 0
    elif Shoulder_Horizontal_Pos < 0:
        print("DUM-Es Shoulder_Horizontal Is Moving Left Towards Middle")
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, True)
        pwm_Shoulder_Horizontal.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Horizontal, True)
        sleep(abs(Shoulder_Horizontal_Pos-(0*1)))
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Horizontal, False)
        pwm_Shoulder_Horizontal.stop()
        print("DUM-E Finished Moving Shoulder_Horizontal Left To Middle")
        Shoulder_Horizontal_Pos = 0
    else:
        print("DUM-Es Shoulder_Horizontal Is Already Located In The Middle")


def Shoulder_Horizontal_Fully_Left():
    if Shoulder_Horizontal_Pos >= -29:
        print("DUM-Es Shoulder_Horizontal_Left Is Moving Fully Left")
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, True)
        pwm_Shoulder_Horizontal.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Horizontal, True)
        sleep(abs(Shoulder_Horizontal_Pos-(-30*1)))
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Horizontal, False)
        pwm_Shoulder_Horizontal.stop()
        print("DUM-E Finished Moving Fully Left")
        Shoulder_Horizontal_Pos = -30
    else:
        print("DUM-Es Shoulder_Horizontal_Left is Already Fully Left")

def Shoulder_Horizontal_Left():
    if Shoulder_Horizontal_Pos >= -29:
        print("DUM-Es Shoulder_Horizontal Is Moving Left")
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, True)
        pwm_Shoulder_Horizontal.ChangeDutyCycle(50)
        GPIO.output(pwm_Shoulder_Horizontal, True)
        sleep(1)
        GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
        GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
        GPIO.output(pwm_Shoulder_Horizontal, False)
        pwm_Shoulder_Horizontal.stop()
        print("DUM-E Finished Shoulder_Horizontal Moving Left")
        Shoulder_Horizontal_Pos = Shoulder_Horizontal_Pos - 1
    else:
        print("DUM-Es Shoulder Vertical is Fully Down")

def LED_On():
    GPIO.output(Claw_LED, True)

def LED_Off():
    GPIO.output(Claw_LED, False)



while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)


    if words == "Claw Open":
        Claw_Open()

    if words == "Claw Fully Open":
        Claw_Fully_Open()

    if words == "Claw Middle":
        Claw_Middle()

    if words == "Claw Fully Close":
        Claw_Fully_Close()

    if words == "Claw Close":
        Claw_Close()        

    if words == "Wrist Up":
        Wrist_Up()        

    if words == "Wrist Fully Up":
        Wrist_Fully_Up()

    if words == "Wrist Middle":
        Wrist_Middle()

    if words == "Wrist Fully Down":
        Wrist_Fully_Down()

    if words == "Wrist Down":
        Wrist_Down()

    if words == "Elbow Down":
        Elbow_Down()

    if words == "Elbow Fully Down":
        Elbow_Fully_Down()

    if words == "Elbow Middle":
        Elbow_Middle()

    if words == "Elbow Fully Up":
        Elbow_Fully_Up()

    if words == "Elbow Up":
        Elbow_Down()

    if words == "Shoulder Up":
        Shoulder_Vertical_Up()

    if words == "Shoulder Middle":
        Shoulder_Vertical_Middle

    if words == "Shoulder Down":
        Shoulder_Vertical_Down()

    if words == "Shoulder Left":
        Shoulder_Horizontal_Left()

    if words == "Rotate Middle":
        Shoulder_Horizontal_Middle()

    if words == "Shoulder Right":
        Shoulder_Horizontal_Right()

    if words == "Light On":
        LED_On()

    if words == "Light Off":
        LED_Off()


    if words == "exit":
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("...")
        sleep(1)
        print("DUM-E Is Sad")
        Claw_Close()
        sleep(1)
        Wrist_Middle()
        sleep(1)
        Elbow_Middle()
        sleep(1)
        Shoulder_Vertical_Middle()
        sleep(1)
        Shoulder_Horizontal_Middle()
        sleep(5)
        print("DUM-E Says Bye Bye")
        break