from time import sleep
import RPi.GPIO as GPIO
from Adafruit_CharLCD import Adafruit_CharLCD

lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_backlight, lcd_columns, lcd_rows = 21, 20, 16, 12, 25, 24, 4, 16, 2


lcd = Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                       lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

try:
    lcd.clear()
    lcd.message('Test\nMessage')

    while True:
        sleep(1)

except:
    print("End")

finally:
    lcd.clear()
    GPIO.cleanup()
