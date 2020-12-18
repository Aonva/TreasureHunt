#Monster die roller
import time

a = 2
b = 0.2
c = 0.08

import random

def monsterfight():
    print("You enter the room and have encountered a hideous beast lunging at you!")
    time.sleep(a)
    print("You draw your weapon and begin to fight!!")
    time.sleep(a)
    print("The creature starts swinging from above.....")
    time.sleep(a)
    #have player roll the die
    num = random.randint(1, 20)
    if num == 20:
        print("You rolled a critical!!!! The Beast is slain" + "You rolled a " + str(num))
    elif num >= 18:
        print("You mortally wounded your target, the creature ran away!!!" + "You rolled a " + str(num))
    elif num >= 10:
        print("You hit your target! the creature ran away!!!" + "You rolled a " + str(num))
        #have the player roll again
    elif num >= 8:
        print("you missed your target and the monster killed you " + "You rolled a " + str(num))
        # have the player roll again
    elif num >= 2:
        print("You have wounded your self! The monster kills you!" + "You rolled a " + str(num))
        # have the player roll again
    else:
        print("The monster had slain you!!! ")
    return num