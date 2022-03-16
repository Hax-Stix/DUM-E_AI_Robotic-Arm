import speech_recognition as sr
#FIXME: Possible Problem Here wit RPi.GPIO
import RPi.GPIO as GPIO
from datetime import date
from time import sleep


GPIO.setmode(GPIO.BOARD)

#GPIO Pins For CLAW
#FIXME: is meant to be 07 even if it looks like a mistake it refers to the pin number on the RASPBERRY PI - Just Add '#' (Comment) to debug
GPIO.setup(07, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
#Claw DC Motor Output
#FIXME: is meant to be 07 even if it looks like a mistake it refers to the pin number on the RASPBERRY PI - Just Add '#' (Comment) to debug
Claw_DC_Motor_1 = (07)
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


def Claw_Open():
    GPIO.output(Claw_DC_Motor_1, True)
    GPIO.output(Claw_DC_Motor_2, False)
    pwm_Claw.ChangeDutyCycle(50)
    GPIO.output(pwm_Claw, True)
    sleep(0.3)
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_2, False)
    GPIO.output(pwm_Claw, False)
    pwm_Claw.stop()
#TODO:
def Claw_Middle():
    if Claw_Pos == 0:
        print("DUM-Es Claw Is Already Located In The Middle")
    elif Wrist_Pos > 0:
        print("DUM-Es Claw Is Moving Towards Middle")
    elif Wrist_Pos < 0:
        print("DUM-Es Claw Is Moving Towards Middle")

def Claw_Close():
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_2, True)
    pwm_Claw.ChangeDutyCycle(50)
    GPIO.output(pwm_Claw, True)
    sleep(0.3)
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(pwm_Claw, False)
    pwm_Claw.stop()


def Wrist_Up():
    GPIO.output(Claw_DC_Motor_1, True)
    GPIO.output(Claw_DC_Motor_2, False)
    pwm_Claw.ChangeDutyCycle(50)
    GPIO.output(pwm_Wrist, True)
    sleep(0.3)
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_2, False)
    GPIO.output(pwm_Wrist, False)
    pwm_Wrist.stop()
#TODO:
def Wrist_Middle():
    if Wrist_Pos == 0:
        print("DUM-Es Wrist Is Already Located In The Middle")
    elif Wrist_Pos > 0:
        print("DUM-Es Wrist Is Moving Towards Middle")
    elif Wrist_Pos < 0:
        print("DUM-Es Wrist Is Moving Towards Middle")

def Wrist_Down():
    GPIO.output(Wrist_DC_Motor_1, False)
    GPIO.output(Wrist_DC_Motor_2, True)
    pwm_Wrist.ChangeDutyCycle(50)
    GPIO.output(pwm_Wrist, True)
    sleep(0.3)
    GPIO.output(Wrist_DC_Motor_1, False)
    GPIO.output(Wrist_DC_Motor_2, False)
    GPIO.output(pwm_Wrist, False)
    pwm_Wrist.stop()


def Elbow_Up():
    GPIO.output(Elbow_DC_Motor_1, True)
    GPIO.output(Elbow_DC_Motor_2, False)
    pwm_Elbow.ChangeDutyCycle(50)
    GPIO.output(pwm_Elbow, True)
    sleep(0.3)
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, False)
    GPIO.output(pwm_Elbow, False)
    pwm_Elbow.stop()
#TODO:
def Elbow_Middle():
    if Elbow_Pos == 0:
        print("DUM-Es Elbow Is Already Located In The Middle")
    elif Elbow_Pos > 0:
        print("DUM-Es Elbow Is Moving Towards Middle")
    elif Elbow_Pos < 0:
        print("DUM-Es Elbow Is Moving Towards Middle")

def Elbow_Down():
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, True)
    pwm_Elbow.ChangeDutyCycle(50)
    GPIO.output(pwm_Elbow, True)
    sleep(0.3)
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, False)
    GPIO.output(pwm_Elbow, False)
    pwm_Elbow.stop()


def Shoulder_Vertical_Up():
    GPIO.output(Shoulder_Vertical_DC_Motor_1, True)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    pwm_Shoulder_Vertical.ChangeDutyCycle(50)
    GPIO.output(pwm_Shoulder_Vertical, True)
    sleep(0.3)
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    GPIO.output(pwm_Shoulder_Vertical, False)
    pwm_Shoulder_Vertical.stop()
#TODO:
def Shoulder_Vertical_Middle():
    if Shoulder_Vertical_Pos == 0:
        print("DUM-Es Shoulder_Vertical Is Already Located In The Middle")
    elif Shoulder_Vertical_Pos > 0:
        print("DUM-Es Shoulder_Vertical Is Moving Towards Middle")
    elif Shoulder_Vertical_Pos < 0:
        print("DUM-Es Shoulder_Vertical Is Moving Towards Middle")

def Shoulder_Vertical_Down():
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, True)
    pwm_Shoulder_Vertical.ChangeDutyCycle(50)
    GPIO.output(pwm_Shoulder_Vertical, True)
    sleep(0.3)
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    GPIO.output(pwm_Shoulder_Vertical, False)
    pwm_Shoulder_Vertical.stop()


def Shoulder_Horizontal_Left():
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, True)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
    pwm_Shoulder_Horizontal.ChangeDutyCycle(50)
    GPIO.output(pwm_Shoulder_Horizontal, True)
    sleep(0.3)
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(pwm_Shoulder_Horizontal, False)
    pwm_Shoulder_Horizontal.stop()
#TODO:
def Shoulder_Horizontal_Middle():
    if Shoulder_Horizontal_Pos == 0:
        print("DUM-Es Shoulder_Horizontal Is Already Located In The Middle")
    elif Shoulder_Horizontal_Pos > 0:
        print("DUM-Es Shoulder_Horizontal Is Moving Towards Middle")
    elif Shoulder_Horizontal_Pos < 0:
        print("DUM-Es Shoulder_Horizontal Is Moving Towards Middle")

def Shoulder_Horizontal_Right():
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, True)
    pwm_Shoulder_Horizontal.ChangeDutyCycle(50)
    GPIO.output(pwm_Shoulder_Horizontal, True)
    sleep(0.3)
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
    GPIO.output(pwm_Shoulder_Horizontal, False)
    pwm_Shoulder_Horizontal.stop()


def LED_On():
    GPIO.output(Claw_LED, True)

def LED_Off():
    GPIO.output(Claw_LED, False)



while True:
    with mic as source:
        audio = r.listen(source)
    words = r.recognize_google(audio)
    print(words)

#TODO:
    if words == "Claw Open" and Claw_Pos == 0:
        print("DUM-Es Claw Opening")
        Claw_Open()
        print("DUM-E Finished Opening Claw")
#TODO:
    if words == "Claw Close":
        print("DUM-Es Claw Closing")
        Claw_Close()        
        print("DUM-E Finished Closing Claw")
#TODO:
    if words == "Wrist Up":
        print("DUM-Es Wrist Up")
        Wrist_Up()        
        print("DUM-E Finished Moving Wrist Up")
#TODO:
    if words == "Wrist Middle":
        print("DUM-Es Wrist Middle")
        Wrist_Middle()
        print("DUM-E Fished Moving Wrist To Middle")
#TODO:
    if words == "Wrist Down":
        print("DUM-Es Wrist Down")
        Wrist_Down()
        print("DUM-E Finished Moving Wrist Down")
#TODO:
    if words == "Elbow Down":
        print("DUM-Es Elbow Down")
        Elbow_Down()
        print("DUM-E Finished Moving Elbow Down")
#TODO:
    if words == "Elbow Middle":
        print("DUM-Es Elbow Middle")
        Elbow_Middle()
        print("DUM-E Finished Moving Elbow to Middle")
#TODO:
    if words == "Elbow Up":
        print("DUM-Es Elbow Up")
        Elbow_Down()
        print("DUM-E Finished Moving Elbow Up")
#TODO:
    if words == "Shoulder Up":
        print("DUM-Es Shoulder Up")
        Shoulder_Vertical_Up()
        print("DUM-E Finished Moving Shoulder Up")
#TODO:
    if words == "Shoulder Middle":
        print("DUM-Es Shoulder Middle")
        Shoulder_Vertical_Middle
        print("DUM-E Finished Moving Shoulder to Middle")
#TODO:
    if words == "Shoulder Down":
        print("DUM-Es Shoulder Down")
        Shoulder_Vertical_Down()
        print("DUM-E Finished Moving Shoulder Down")
#TODO:
    if words == "Shoulder Left":
        print("DUM-Es Shoulder Left")
        Shoulder_Horizontal_Left()
        print("DUM-E Finished Moving Shoulder Left")
#TODO:
    if words == "Rotate Middle":
        print("DUM-Es Rotating To Middle")
        Shoulder_Horizontal_Middle()
        print("DUM-E Finished Rotating To Middle")
#TODO:
    if words == "Shoulder Right":
        print("DUM-Es Shoulder Right")
        Shoulder_Horizontal_Right()
        print("DUM-E Finished Moving Shoulder Right")

    if words == "Light On":
        print("DUM-Es Light On")
        LED_On()
        print("DUM-E Finished Turning Light On")

    if words == "Light Off":
        print("DUM-Es Light Off")
        LED_Off()
        print("DUM-E Finished Turning Light Off")


#TODO:
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