# Slot Machine Simulator - CS530 Group 6

The Slot Machine Simulator is a hardware prototype which interfaces with an LCD screen, coin acceptor, 2 buttons, and 9 LEDs using Python.

# How to use

1. Enter quarters into coin acceptor.
2. When ready, press the Start button to roll.
3. The program randomly generates 3 numbers between 1-3 and reflects them onto the 9 LEDs.

- If 3 LEDs match, player receives 2.0x their initial bet.
- If 2 LEDs match, player receives 1.5x their initial bet.
- If no LEDs match, the player doesn't receive a payout.

4. When prompted, press the Start button to play again or Exit button to end play.

## Requirements

- Raspberry Pi Model 3B+
- 16x2 LCD Screen
- Coin Acceptor Model CH-926
- 2 buttons
- 3 Red, 3 Green, 3 Blue LEDs
- 9 220Ω Resistors
- T-Cobbler
- Breadboard
- Jumper Cables
- 12V 1A Power Supply (For coin acceptor)
- 5V 2.5A Power Supply (For Raspberry Pi)

## Loading SlotMachine.py on Raspberry Pi Startup

In Raspberry Pi CLI, access rc.local file:

```bash
  sudo nano /etc/rc.local
```

Add the following to the end of the file:

```bash
  sudo python /home/pi/SlotMachine.py &
  exit 0
```

Press CTRL+X then Y to save changes.
