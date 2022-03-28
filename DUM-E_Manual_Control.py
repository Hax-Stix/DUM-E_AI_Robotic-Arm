import RPi.GPIO as GPIO
#INFO:RPi.GPIO Librarry Not Avaliable On Anyhting Other Than RPI Boards
from time import sleep

GPIO.setmode(GPIO.BOARD)

#GPIO Pins For CLAW
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
#Claw DC Motor Output
Claw_DC_Motor_1 = (7)
Claw_DC_Motor_2 = (11)
#Claw PWM Control
pwm_pin_Claw = (15)
pwm_Claw=GPIO.PWM(pwm_pin_Claw, 100)
pwm_Claw.start(0)

#GPIO Pins For Wrist
GPIO.setup(13, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
#Wrist DC Motor Output
Wrist_DC_Motor_1 = (13)
Wrist_DC_Motor_2 = (12)
#Wrist PWM Control
pwm_pin_Wrist = (16)
pwm_Wrist=GPIO.PWM(pwm_pin_Wrist, 100)
pwm_Wrist.start(0)

#GPIO Pins For Elbow
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
#Elbow DC Motor Output
Elbow_DC_Motor_1 = (18)
Elbow_DC_Motor_2 = (22)
#Elbow PWM Control
pwm_pin_Elbow = (23)
pwm_Elbow=GPIO.PWM(pwm_pin_Elbow, 100)
pwm_Elbow.start(0)

#GPIO Pins For Shoulder Vertical
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
#Shoulder Vertical DC Motor Output
Shoulder_Vertical_DC_Motor_1 = (24)
Shoulder_Vertical_DC_Motor_2 = (26)
#Shoulder Vertical PWM Control
pwm_pin_Shoulder_Vertical = (19)
pwm_Shoulder_Vertical=GPIO.PWM(pwm_pin_Shoulder_Vertical, 100)
pwm_Shoulder_Vertical.start(0)

#GPIO Pins for Shoulder Horizontal 
GPIO.setup(21, GPIO.OUT)
GPIO.setup(37, GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
#Shoulder Horizontal DC Motor Output
Shoulder_Horizontal_DC_Motor_1 = (21)
Shoulder_Horizontal_DC_Motor_2 = (37)
#Shoulder Horizontal PWM Control
pwm_pin_Shoulder_Horizontal = (40)
pwm_Shoulder_Horizontal=GPIO.PWM(pwm_pin_Shoulder_Horizontal, 100)
pwm_Shoulder_Horizontal.start(0)


#GPIO.setup
GPIO.setup(38, GPIO.OUT)
#Claw LED Output
Claw_LED = 38

time = 0
speed = 0
motion = ""

def Claw_Open():
    print("DUM-Es Claw Is Opening")
    GPIO.output(int(Claw_DC_Motor_1), True)
    GPIO.output(int(Claw_DC_Motor_2), False)
    pwm_Claw.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Claw), True)
    sleep(int(time))
    GPIO.output(int(Claw_DC_Motor_1), False)
    GPIO.output(int(Claw_DC_Motor_2), False)
    GPIO.output((pwm_pin_Claw), False)
    pwm_Claw.stop()
    print("DUM-E Finished Opening Claw")

def Claw_Close():
    print("DUM-Es Claw Is Closing")
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_2, True)
    pwm_Claw.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Claw), True)
    sleep(int(time))
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output(Claw_DC_Motor_1, False)
    GPIO.output((pwm_pin_Claw), False)
    pwm_Claw.stop()
    print("DUM-E Finished Closing Claw")

def Wrist_Up():
    print("DUM-Es Wrist Is Moving Up")
    GPIO.output(Wrist_DC_Motor_1, True)
    GPIO.output(Wrist_DC_Motor_2, False)
    pwm_Wrist.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Wrist), True)
    sleep(int(time))
    GPIO.output(Wrist_DC_Motor_1, False)
    GPIO.output(Wrist_DC_Motor_2, False)
    GPIO.output((pwm_pin_Wrist), False)
    pwm_Wrist.stop()
    print("DUM-E Finished Moving Wrist Up")

def Wrist_Down():
    print("DUM-Es Wrist is Moving Down")
    GPIO.output(Wrist_DC_Motor_1, False)
    GPIO.output(Wrist_DC_Motor_2, True)
    pwm_Wrist.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Wrist), True)
    sleep(int(time))
    GPIO.output(Wrist_DC_Motor_1, False)
    GPIO.output(Wrist_DC_Motor_2, False)
    GPIO.output((pwm_pin_Wrist), False)
    pwm_Wrist.stop()
    print("DUM-E Finished Moving Wrist Down")

def Elbow_Up():
    print("DUM-Es Elbow is moving Up")
    GPIO.output(Elbow_DC_Motor_1, True)
    GPIO.output(Elbow_DC_Motor_2, False)
    pwm_Elbow.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Elbow), True)
    sleep(int(time))
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, False)
    GPIO.output((pwm_pin_Elbow), False)
    pwm_Elbow.stop()
    print("DUM-E Finished Moving Elbow up")
    
def Elbow_Down():
    print("DUM-Es Elbow Is Moving Down")
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, True)
    pwm_Elbow.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Elbow), True)
    sleep(int(time))
    GPIO.output(Elbow_DC_Motor_1, False)
    GPIO.output(Elbow_DC_Motor_2, False)
    GPIO.output((pwm_pin_Elbow), False)
    pwm_Elbow.stop()
    print("DUM-E Finished Moving Elbow Down")

def Shoulder_Vertical_Down():
    print("DUM-Es Shoulder_Vertical Is Moving Down")
    GPIO.output(Shoulder_Vertical_DC_Motor_1, True)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    pwm_Shoulder_Vertical.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Shoulder_Vertical), True)
    sleep(int(time))
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    GPIO.output((pwm_pin_Shoulder_Vertical), False)
    pwm_Shoulder_Vertical.stop()
    print("DUM-E Finished Moving Shoulder_Vertical Down")

def Shoulder_Vertical_Up():
    print("DUM-Es Shoulder_Vertical Is Moving Up")
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, True)
    pwm_Shoulder_Vertical.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Shoulder_Vertical), True)
    sleep(int(time))
    GPIO.output(Shoulder_Vertical_DC_Motor_1, False)
    GPIO.output(Shoulder_Vertical_DC_Motor_2, False)
    GPIO.output((pwm_pin_Shoulder_Vertical), False)
    pwm_Shoulder_Vertical.stop()
    print("DUM-E Finished Moving Up")

def Shoulder_Horizontal_Right():
    print("DUM-Es Shoulder_Horizontal Is Moving Right")
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, True)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
    pwm_Shoulder_Horizontal.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Shoulder_Horizontal), True)
    sleep(int(time))
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output((pwm_pin_Shoulder_Horizontal), False)
    pwm_Shoulder_Horizontal.stop()
    print("DUM-E Finished Moving Shoulder_Horizontal Right")

def Shoulder_Horizontal_Left():
    print("DUM-Es Shoulder_Horizontal Is Moving Left")
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, True)
    pwm_Shoulder_Horizontal.ChangeDutyCycle(int(speed))
    GPIO.output((pwm_pin_Shoulder_Horizontal), True)
    sleep(int(time))
    GPIO.output(Shoulder_Horizontal_DC_Motor_1, False)
    GPIO.output(Shoulder_Horizontal_DC_Motor_2, False)
    GPIO.output((pwm_pin_Shoulder_Horizontal), False)
    pwm_Shoulder_Horizontal.stop()
    print("DUM-E Finished Shoulder_Horizontal Moving Left")

def LED_On():
    print("LED On")
    GPIO.output(Claw_LED, True)

def LED_Off():
    print("LED Off")
    GPIO.output(Claw_LED, False)


while True:
    time = input("Enter Time:")
    speed = input("Enter Speed:")
    print("1. Claw Open\n""2. Claw Close\n""3. Wrist Up\n""4. Wrist Down\n""5. Elbow Up\n""6. Elbow Down\n""7. Shoulder Vertical Up\n""8. Shoulder Vertical Down\n""9. Shoulder Horizontal Left\n""10. Shoulder Horizontal Right\n""11. LED On\n""12. LED Off\n""13. EXIT\n")
    motion = int(input("Enter Motion:"))

    if motion == 1:
        Claw_Open()
        motion = 0

    elif motion == 2:
        Claw_Close()
        motion = 0

    elif motion == 3:
        Wrist_Up()
        motion = 0

    elif motion == 4:
        Wrist_Down()
        motion = 0

    elif motion == 5:
        Elbow_Up()
        motion = 0

    elif motion == 6:
        Elbow_Down()
        motion = 0

    elif motion == 7:
        Shoulder_Vertical_Up()
        motion = 0

    elif motion == 8:
        Shoulder_Vertical_Down()
        motion = 0

    elif motion == 9:
        Shoulder_Horizontal_Left()
        motion = 0

    elif motion == 10:
        Shoulder_Horizontal_Right()
        motion = 0
    
    elif motion == 11:
        LED_On()
        motion = 0
    
    elif motion == 12:
        LED_Off()
        motion = 0

    elif motion == 13:
        motion = 0
        break