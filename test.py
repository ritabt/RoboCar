# import RPi.GPIO as GPIO
# from time import sleep
#
# front_back_right_1 = 27
# front_back_right_2 = 22
# front_in3 = 23
# front_in4 = 24
# back_back_right_1 = 6
# back_back_right_2 = 13
# back_in3 = 19
# back_in4 = 26

import RPi.GPIO as GPIO
from time import sleep

back_right_1 = 27
back_right_2 = 22
back_right_en = 25
back_left_1 = 24
back_left_2 = 23
back_left_en = 4
front_right_1 = 13
front_right_2 = 26
front_right_en = 10
front_left_1 = 6
front_left_2 = 5
front_left_en = 9
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def GPIO_setup(in1, in2, en):
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    p = GPIO.PWM(en, 1000)
    p.start(25)
    return p

p_back_right = GPIO_setup(back_right_1, back_right_2, back_right_en)
p_back_left = GPIO_setup(back_left_1, back_left_2, back_left_en)
p_front_right = GPIO_setup(front_right_1, front_right_2, front_right_en)
p_front_left = GPIO_setup(front_left_1, front_left_2, front_left_en)

all_in1 = [back_right_1, back_left_1, front_right_1, front_left_1]
all_in2 = [back_right_2, back_left_2, front_right_2, front_left_2]
all_p = [p_back_right, p_back_left, p_front_right, p_front_left]

print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")

def forward(all_in1, all_in2):
    for in1, in2 in zip(all_in1, all_in2):
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)

def backward(all_in1, all_in2):
    for in1, in2 in zip(all_in1, all_in2):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)

def stop(all_in1, all_in2):
    for in1, in2 in zip(all_in1, all_in2):
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)

def p_speed(x, all_p):
    for p in all_p:
        p.ChangeDutyCycle(x)

while (1):

    x = raw_input()

    if x == 'r':
        print("run")
        if (temp1 == 1):
            forward(all_in1, all_in2)
            print("forward")
            x = 'z'
        else:
            backward(all_in1, all_in2)
            print("backward")
            x = 'z'


    elif x == 's':
        print("stop")
        stop(all_in1, all_in2)
        x = 'z'

    elif x == 'f':
        print("forward")
        forward(all_in1, all_in2)
        temp1 = 1
        x = 'z'

    elif x == 'b':
        print("backward")
        backward(all_in1, all_in2)
        temp1 = 0
        x = 'z'

    elif x == 'l':
        print("low")
        p_speed(25, all_p)
        x = 'z'

    elif x == 'm':
        print("medium")
        p_speed(50, all_p)
        x = 'z'

    elif x == 'h':
        print("high")
        p_speed(75, all_p)
        x = 'z'


    elif x == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")