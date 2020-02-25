import time
import random

monsters = ["Gorgon", "Kikimora", "Bruxa"]

mymonster = random.choice(monsters)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + mymonster + "is somewhere around here, and has been terrifying the nearby "
                                                     "village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.")


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a " + mymonster)
    print_pause("Eep! This is the " + mymonster + "'s house!")
    print_pause("The " + mymonster + " attacks you!")
    print_pause("You feel a bit under-prepared for this, what with only have a tiny dagger.")
    print_pause("Would you like to (1) fight or (2) run away?")
    print_pause()
    choices()


def cave():
    print_pause()


def choices():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    print_pause("(Please enter 1 or 2.)")
    choice = input("1. Knock on the door of the house."
                   "2. Peer into the cave.")
    while False:
        if choice == '1':
            house()
        if choice == '2':
            cave()
        else:
            print_pause("(Please enter 1 or 2.)")


def play_game():
    intro()
    house()
    choices()


play_game()
