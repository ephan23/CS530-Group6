import RPi.GPIO as GPIO
import time

credits = 0

# Declare coin acceptor GPIO pin
coin_input = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(coin_input, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    input_state = GPIO.input(coin_input)

    while True:
        time.sleep(0.1)

        # If coin inserted and accepted
        if input_state == False:
            credits += 25       # Quarter accepted
            print(credits)      # Display credits for debug

except:
    print("Exit")

finally:
    GPIO.clear()
