import RPi.GPIO as GPIO
from random import randrange

from Adafruit_CharLCD import Adafruit_CharLCD

lcd_rs        = 21
lcd_en        = 20
lcd_d4        = 12
lcd_d5        = 25
lcd_d6        = 24
lcd_d7        = 23
lcd_backlight = 4
lcd_columns = 16
lcd_rows = 2

R1,G1,B1,R2,G2,B2,R3,G3,B3 = 4,17,27,22,5,6,13,19,26

GPIO.setmode(GPIO.BCM)
GPIO.setup((R1,G1,B1,R2,G2,B2,R3,G3,B3), GPIO.OUT)

lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


def rollHandler():
    roll1 = randrange(3) + 1
    roll2 = randrange(3) + 1
    roll3 = randrange(3) + 1
    
    print(roll1, roll2, roll3)
    
    GPIO.output((R1,G1,B1,R2,G2,B2,R3,G3,B3), GPIO.LOW)
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
    return roll1,roll2,roll3

response = "y"

try:
    lcd.clear()
    
    while response == "y":
        rollHandler()
            
        response = input()
        
        
        
except:
    print("nah")


finally:
    lcd.clear()
    GPIO.cleanup()

