from random import randrange

def calculatePayout(bet,slot1,slot2,slot3):
    #Check number of matches
    if slot1 == slot2:
        if slot2 == slot3:
            bet *= 2     #Three match, 2.0x bet
            lcd.message("All three numbers matched.", end='')
        else:
            bet *= 1.5   #Two match, 1.5x bet
            lcd.message("Two numbers matched.", end='')
    elif slot2 == slot3:
        bet *= 1.5       #Two match, 1.5x bet
        lcd.message("Two numbers matched.", end='')
    elif slot1 == slot3:
        bet *= 1.5       #Two match, 1.5x bet
        lcd.message("Two numbers matched.", end='')
    else:
        bet = 0          #No match, 0x bet
        lcd.message("No numbers matched.", end='')
    
    return int(bet)

credits = 1000  # Default credits
response = "y"  # Initialize 'play again' response to "y" to ensure while loop executes at least onece, emulating a 'do while' loop

lcd.message("Welcome to the slot machine simulator!")

while response == "y":
    #Prompt user for bet
    lcd.message("You have", credits, "credits. How much would you like to bet?")

    bet = int(input())
    lcd.message()

    #Check if bet is valid
    while (bet < 0) or (bet > credits):
        lcd.message("Your bet is invalid. Please try again.")
        lcd.message("You have", credits, "credits. How much would you like to bet?")
        bet = int(input())
        lcd.message()

    credits = credits - bet

    #Simulate slot rolling
    lcd.message("Rolling!")
    slot1 = randrange(3) + 1
    slot2 = randrange(3) + 1
    slot3 = randrange(3) + 1
    lcd.message("You rolled:", slot1, slot2, slot3)

    payout = calculatePayout(bet, slot1, slot2, slot3)

    #Output bet and update credits
    credits += payout
    lcd.message(" You win", payout, "credits. New balance:",credits,"credits")

    #If user has credits remaining, prompt to play again, exit otherwise
    if credits > 0:
        lcd.message("Would you like to play again? (y/n)")
        response = input()
        lcd.message()
    else:
        lcd.message("No more credits detected.", end='')
        response = "n"

lcd.message("Goodbye!")