from Adafruit_CharLCD import Adafruit_CharLCD
from random import randrange

import RPi.GPIO as GPIO
import sys
import time

# Declare default variables
credits = 0
playAgain = True

# LCD GPIO Pin Variables
lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_backlight, lcd_columns, lcd_rows = 21, 20, 16, 12, 25, 24, 4, 16, 2

# LED Lights GPIO Pin Variables
R1, G1, B1, R2, G2, B2, R3, G3, B3 = 4, 17, 27, 22, 5, 6, 13, 19, 26

# Button GPIO Pin Variables
btnSelect, btnExit = 23, 18

# Coin Acceptor GPIO Pin Variable
coinSlot = 14

# Set GPIO Mode
GPIO.setmode(GPIO.BCM)

# Setup GPIO LED Pins
GPIO.setup((R1, G1, B1, R2, G2, B2, R3, G3, B3), GPIO.OUT)

# Setup GPIO Button Pins
GPIO.setup((btnSelect, btnExit, coinSlot), GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Setup LCD
lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                       lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


# Function that will display a welcome message at the start of the program
def welcomeMessage():
    lcd.clear()
    lcd.message("Welcome to the\nSlot Machine!")
    time.sleep(2)

    lcd.clear()
    lcd.message("Insert coins or\nPress Start")


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


# Function to handle calculating payout
def calculatePayout(bet, slot1, slot2, slot3):
    lcd.clear()

    if (slot1 == slot2):
        if (slot2 == slot3):
            bet *= 2  # Three match, 2.0x bet
            lcd.message("All numbers match\nPayout: " + str(bet))
        else:
            bet *= 1.5  # Two match, 1.5x bet
            lcd.message("2 numbers match\nPayout: " + str(bet))
    elif (slot2 == slot3):
        bet *= 1.5  # Two match, 1.5x bet
        lcd.message("2 numbers match\nPayout: " + str(bet))
    elif (slot1 == slot3):
        bet *= 1.5  # Two match, 1.5x bet
        lcd.message("2 numbers match\nPayout: " + str(bet))
    else:
        bet = 0  # No match, 0x bet
        lcd.message("No numbers matched\nPayout: " + str(bet))

    return bet


# Main function

try:
    GPIO.output((R1, G1, B1, R2, G2, B2, R3, G3, B3),
                GPIO.LOW)     # Set LED pins to OFF
    welcomeMessage()

    # Main Loop
    while True:
        # Set input_state to coinSlot current state
        input_state = GPIO.input(coinSlot)

        # Set start to btnSelect current state
        start = GPIO.input(btnSelect)

        time.sleep(0.1)

        # Condition if coin is inserted
        if input_state == False:
            print("coin inserted")
            credits += 25
            lcd.clear()
            lcd.message("Current bet:\n" + str(credits))
            time.sleep(2)
            lcd.clear()
            lcd.message("Insert coins or\nPress Start")

        # Condition if Start button pressed
        if start == False:
            if credits != 0:
                slotList = rollHandler()
                credits = calculatePayout(
                    credits, slotList[0], slotList[1], slotList[2])
                print("button pressed")
                time.sleep(10)

                lcd.clear()
                lcd.message("Play again?\n1.No 2.Yes")
                time.sleep(1)
                playAgain = False

            else:
                lcd.clear()
                lcd.message("No credits\nInsert coins.")

        # Play Again loop
        while playAgain == False:
            start = GPIO.input(btnSelect)
            exit = GPIO.input(btnExit)

            time.sleep(0.1)

            if exit == False:
                lcd.clear()
                lcd.message("Thank you!\nWinnings: " + str(credits))
                time.sleep(5)
                sys.exit()      # Exit program

            if start == False:
                print("start pressed")
                time.sleep(1)
                lcd.clear()
                lcd.message("Playing again")
                time.sleep(1)
                lcd.clear()

                lcd.message("Insert coins or\nPress Start")
                GPIO.output((R1, G1, B1, R2, G2, B2, R3, G3, B3),
                            GPIO.LOW)     # Set LEDs to OFF
                credits = 0
                playAgain = True


except KeyboardInterrupt:
    print("Exited using CTRL+C")

finally:
    # Executes cleanup when program exits
    lcd.clear()
    GPIO.cleanup()
