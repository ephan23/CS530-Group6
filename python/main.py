import RPi.GPIO as GPIO
from random import randrange

from Adafruit_CharLCD import Adafruit_CharLCD

# LCD GPIO Pin Variables
lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_backlight, lcd_columns, lcd_rows = 21, 20, 16, 12, 25, 24, 4, 16, 2

# LED Lights GPIO Pin Variables
R1, G1, B1, R2, G2, B2, R3, G3, B3 = 4, 17, 27, 22, 5, 6, 13, 19, 26

# Button GPIO Pin Variables
btnSelect, btnExit = 23, 18

# Set GPIO Mode
GPIO.setmode(GPIO.BCM)

# Setup GPIO LED Pins
GPIO.setup((R1, G1, B1, R2, G2, B2, R3, G3, B3), GPIO.OUT)

# Setup GPIO Button Pins
GPIO.setup((btnSelect, btnExit), GPIO.OUT)

# Setup LCD
lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                       lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


# Function to roll number between random range 1-3. Returns 3 integers
def rollHandler():
    roll1 = randrange(3) + 1
    roll2 = randrange(3) + 1
    roll3 = randrange(3) + 1

    print(roll1, roll2, roll3)

    GPIO.output((R1, G1, B1, R2, G2, B2, R3, G3, B3), GPIO.LOW)
    lcd.clear()

    if (roll1 == 1):
        GPIO.output(R1, GPIO.HIGH)
    elif (roll1 == 2):
        GPIO.output(G1, GPIO.HIGH)
    elif (roll1 == 3):
        GPIO.output(B1, GPIO.HIGH)

    if (roll2 == 1):
        GPIO.output(R2, GPIO.HIGH)
    elif (roll2 == 2):
        GPIO.output(G2, GPIO.HIGH)
    elif (roll2 == 3):
        GPIO.output(B2, GPIO.HIGH)

    if (roll3 == 1):
        GPIO.output(R3, GPIO.HIGH)
    elif (roll3 == 2):
        GPIO.output(G3, GPIO.HIGH)
    elif (roll3 == 3):
        GPIO.output(B3, GPIO.HIGH)

    message = str(roll1) + str(roll2) + str(roll3)

    lcd.message(message)
    return roll1, roll2, roll3


# Set default response to "y"
# response = "y"

try:
    lcd.clear()

    while True:
        start = GPIO.input(btnSelect)

        if start == False:
            rollHandler()
            time.sleep(1)


except:
    print("Exited")


finally:
    lcd.clear()
    GPIO.cleanup()
