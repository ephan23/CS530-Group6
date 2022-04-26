from time import sleep
import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD

# Declare LED GPIO Pins
R1, G1, B1, R2, G2, B2, R3, G3, B3 = 4, 17, 27, 22, 5, 6, 13, 19, 26

# Declare Button GPIO Pin
btn = 23

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    state = GPIO.input(btn)

    while True:
        sleep(1)

        if state == False:
            # Turn on all LEDs
            GPIO.output(R1, GPIO.HIGH)
            GPIO.output(G1, GPIO.HIGH)
            GPIO.output(B1, GPIO.HIGH)

            GPIO.output(R2, GPIO.HIGH)
            GPIO.output(G2, GPIO.HIGH)
            GPIO.output(B2, GPIO.HIGH)

            GPIO.output(R3, GPIO.HIGH)
            GPIO.output(G3, GPIO.HIGH)
            GPIO.output(B3, GPIO.HIGH)

            sleep(2)

            # Turn off all LEDs after 2 seconds
            GPIO.output(R1, GPIO.LOW)
            GPIO.output(G1, GPIO.LOW)
            GPIO.output(B1, GPIO.LOW)

            GPIO.output(R2, GPIO.LOW)
            GPIO.output(G2, GPIO.LOW)
            GPIO.output(B2, GPIO.LOW)

            GPIO.output(R3, GPIO.LOW)
            GPIO.output(G3, GPIO.LOW)
            GPIO.output(B3, GPIO.LOW)

except:
    print("Exit")

finally:
    GPIO.cleanup()
