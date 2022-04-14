from random import randrange

credits = 1000  # Default credits
response = "y"  # Initialize 'play again' response to "y" to ensure while loop executes at least onece, emulating a 'do while' loop

print("Welcome to the slot machine simulator!")

while response == "y":
    #Prompt user for bet
    print("You have", credits, "credits. How much would you like to bet?")

    bet = int(input())
    print()

    #Check if bet is valid
    while (bet < 0) or (bet > credits):
        print("Your bet is invalid. Please try again.")
        print("You have", credits, "credits. How much would you like to bet?")
        bet = int(input())
        print()

    credits = credits - bet

    #Simulate slot rolling
    print("Rolling!")
    slot1 = randrange(3) + 1
    slot2 = randrange(3) + 1
    slot3 = randrange(3) + 1
    print("You rolled:", slot1, slot2, slot3)

    #Check number of matches
    if slot1 == slot2:
        if slot2 == slot3:
            bet *= 2     #Three match, 2.0x bet
            print("All three numbers matched.", end='')
        else:
            bet *= 1.5   #Two match, 1.5x bet
            print("Two numbers matched.", end='')
    elif slot2 == slot3:
        bet *= 1.5       #Two match, 1.5x bet
        print("Two numbers matched.", end='')
    elif slot1 == slot3:
        bet *= 1.5       #Two match, 1.5x bet
        print("Two numbers matched.", end='')
    else:
        bet = 0          #No match, 0x bet
        print("No numbers matched.", end='')

    #Output bet and update credits
    bet = int(bet)
    credits += bet
    print(" You win", bet, "credits. New balance:",credits,"credits")

    #If user has credits remaining, prompt to play again, exit otherwise
    if credits > 0:
        print("Would you like to play again? (y/n)")
        response = input()
        print()
    else:
        print("No more credits detected.", end='')
        response = "n"

print("Goodbye!")