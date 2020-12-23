#Monster die roller
import time

a = 2
b = 0.2
c = 0.08

import random

def monsterfight():
    print()
    print("You enter the room and suddenly a hideous beast lunges at you!")
    time.sleep(a)
    print("The creature starts swinging from above.....")
    time.sleep(a)
    #have player roll the die
    num = random.randint(1, 20)
    if num == 20:
        print("You draw your weapon and begin to fight!!")
        print()
        print("You rolled a critical!!!! The Beast is slain. " + "You rolled a " + str(num))
    elif num >= 18:
        print("You draw your weapon and begin to fight!!")
        print()
        print("You mortally wounded your target, the creature ran away!!! " + "You rolled a " + str(num))
    elif num >= 10:
        print("You draw your weapon and begin to fight!!")
        print()
        print("You hit your target! Scaring the creature and it run's away!!! " + "You rolled a " + str(num))
        #have the player roll again
    elif num >= 8:
        print("You missed your target buy slipping on some rotting food and the monster kill's you!! " + "You rolled a " + str(num))
        # have the player roll again
    elif num >= 2:
        print("As you draw your weapon you injure yourself by cutting your hand off! The monster kills you!! " + "You rolled a " + str(num))
        # have the player roll again
    else:
        print("Startled by the beast you are unable to move, frozen by fear!!")
        print("Taking the opportunity the monster kills you instantly!!! ")
    return num