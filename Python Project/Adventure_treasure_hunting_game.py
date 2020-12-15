### Treasure hunt Dungeon game

#time delay for reading ease and game feel effect.

import time

a = 2
b = 0.2
c = 0.08


#Monster fight and die roller random function


#sinarios of each room

def showinstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [direction option's north, south, east, west]
  get [item]
''')


def showstatus():
    # print the player's current status
    print('---------------------------')
    print('You are at ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


# a dictionary linking a room to other rooms

# This is the begging of game coding story

        # start the player at the cave entrance

        print(" Treasure Hunter Look!!! ")
        time.sleep(a)
        print()
        print("       __      _")
        print("      /__\__  //")
        print("     //_____\///")
        print("    _| /-_-\)|/__")
        print("  (___ \ _ //___ \ ")
        print("  (  |\ \_/// * \ \ ")
        print("   \_| \_((*   *)) ")  # Knight
        print("   ( |__|_\ \  */ / ")
        print("   (o/  _  \_*_/_/")
        print("   //\__|__/\ ")
        print("  // |  | |  | ")
        print(" //  _\ | |___) ")
        print("//  (___| ")
        print()
        print()
        time.sleep(a)
        print("You begin to hear a deep rumbling of the earth.")
        time.sleep(a)
        print("You suddenly see the cave")
        time.sleep(a)
        print("You enter the dark cave.")
        time.sleep(a)
        print("As you emerge from the entry way, your eye's begin to focus.")
        time.sleep(a)
        print("The ground beneath you begins to rumble, shaking the entire cavern. Debris fall from every direction.")
        time.sleep(a)
        print("Suddenly!!!  Three paths are revealed:")
        print()
        print("Path #1: Move forward through the debris to your right of the cave, into the light.")
        time.sleep(a)
        print("Path #2: Explore the depths of the rear of the cave, into the darkness.")
        time.sleep(a)
        print(
            "Path #3: Climb down the overgrowth of vines into a bottomless hole in the ground to your left of the cave.")
        print()

#Main Function ###
print()
print()
print("       __      _")
print("      /__\__  //")
print("     //_____\///")
print("    _| /-_-\)|/__")
print("  (___ \ _ //___ \ ")
print("  (  |\ \_/// * \ \ ")  #Knight
print("   \_| \_((*   *)) ")
print("   ( |__|_\ \  */ / ")
print("   (o/  _  \_*_/_/")
print("   //\__|__/\ ")
print("  // |  | |  | ")
print(" //  _\ | |___) ")
print("//  (___| ")
time.sleep(a)
print("Let us begin a Treasure hunting adventure!!!!!")
time.sleep(a)

# start the player at the cave entrance

showinstructions()

startgame = input("Would you like to start the game? (Y?N): ")
if startgame == 'n' or startgame == 'N':
    print("Maybe next time.")
if startgame == 'y' or startgame == 'Y':
    print("Let us begin the adventure!!!!!")
    intro()

