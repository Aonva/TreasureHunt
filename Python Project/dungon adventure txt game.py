#Dungon Text Game
import dragon as dragon

import monsterdieroller
import sys
import time
a = 2
b = 0.2
c = 0.08
from time import sleep

def showinstructions():
    # print a main menu and the commands
    print('''
Treasure Hunt Game
========
Commands:
  Type in - go [direction option's north, south, east, west]
            
========
You start from the north going south in to the dungeon:
''')
    time.sleep(a)
    print()
    print("       __      _")
    print("      /__\__  //")
    print("     //_____\///")
    print("    _| /-_-\)|/__")
    print("  (___ \ _ //___ \ ")
    print("  (  |\ \_/// * \ \ ")  # Knight
    print("   \_| \_((*   *)) ")
    print("   ( |__|_\ \  */ / ")
    print("   (o/  _  \_*_/_/")
    print("   //\__|__/\ ")
    print("  // |  | |  | ")
    print(" //  _\ | |___) ")
    print("//  (___| ")
    print()
    time.sleep(a)
    print("Let us begin a Treasure hunting adventure!!!!!")
    time.sleep(a)
    print()


def showstatus():
    # print the player's current status
    print('--------------------')
    print('You are at ' + currentRoom)
    time.sleep(a)
    print('''
    ========
    Commands:
    Type in - go [direction option's north, south, east, west]
            
    ========''')
    # print the current inventory
    #print('Inventory : ' + str(inventory))
    #time.sleep(a)
    f = open(rooms[currentRoom]['story'],"r")
    txt = f.read()
    f.close()
    for char in txt:
        sleep(.05)
        sys.stdout.write(char)
    # print an item if there is one
    #if "item" in rooms[currentRoom]:
        #print('You see a ' + rooms[currentRoom]['item'])
    print()
    print("--------------------")

#main game start here
# an inventory, which is initially empty
#inventory = []


# a dictionary linking a room to other rooms
rooms = {

    'entrance' : {
        'story' : 'entrance.txt',
        'west' : 'room1',
        'south' : 'room2',
        'east' : 'room3'
        },
    'room1' :{
        'story' : 'room1.txt',
        'south' : 'room6',
        'item' : "trap"
        },
    'room2' : {
        'story' : 'room2.txt',
        'south' : 'room5',
        'item' : 'monster'
        },
    'room3' : {
        'story': 'room3.txt',
        'south' : 'room4',
        },
    'room4' : {
        'story' : 'room4.txt',
        'west' : 'room5',
        'south' : 'room9',
        'item' : 'sword'
        },
    'room5' : {
        'story' : 'room5.txt',
        'west' : 'room6',
        'south' : 'room8',
        'east' : 'room4'
        },
    'room6' : {
        'story' : 'room6.txt',
        'north' : 'room1',
        'south' : 'room7'
        },
    'room7' : {
        'story' : 'room7.txt',
        'north' : 'room6',
        'south' : 'room10',
        'east' : 'room8',
        'item': 'monster'
        },
    'room8' : {
        'story' : 'room8.txt',
        'west' : 'room7',
        'north' : 'room5',
        'east' : 'room9',
        'item' : 'trap'
        },
    'room9' : {
        'story' : 'room9.txt',
        'west' : 'room8',
        'north' : 'room4',
        'south' : 'room11',
        'item' : 'MysticalOrb'
        },
    'room10' : {
        'story' : 'treasure.txt',
        'north' : 'room7'
        },
    'room11' : {
        ''
        'story' : 'dragon.txt',
        'north' : 'room9',
        'item' : 'dragon'
                 },
    }

# start the player at the cave entrance
currentRoom = 'entrance'

showinstructions()

# loop forever

while True:

    showstatus()

    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('What direction would you like to go? ')
        # let them know they didn't type anything or typed the wrong thing
        if move.lower().split(" ", 1)[0] not in ['go', 'get']:
            print('That was not a valid entry. Please type a direction such as north, south, east, or west. ')
            move = ''
    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            if rooms[currentRoom][move[1]] == 'room11':
                #Define how a player loses
                time.sleep(a)
                lose = open("dragon.txt", "r")
                print(lose.read())
                txt = lose.read()
                lose.close()
                for char in txt:
                    sleep(.05)
                    sys.stdout.write(char)
                drag = open('dragon.askii')
                print(drag.read())
                print('----------------------')
                print()
                startgame = input("Would you like to re-start the game? (Y?N): ")
                if startgame == 'n' or startgame == 'N':
                    print("Maybe next time. Good Bye. ")
                    break
                if startgame == 'y' or startgame == 'Y':
                    print("Let us begin the adventure!!!!!")
                    currentRoom = 'entrance'
                    continue
            ## Define how a player can win
            if rooms[currentRoom][move[1]] == 'room10':
                time.sleep(a)
                win = open("treasure.txt", "r")
                print(win.read())
                txt = win.read()
                win.close()
                for char in txt:
                    sleep(.05)
                    sys.stdout.write(char)
                print('----------------------')
                print()
                print('...!YOU WIN!...')
                break
            else:
                # set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')
    ## if they type 'get' first
    #if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        ##inventory += rooms[currentRoom].get("item")
            # display a helpful message
            #print(rooms[currentRoom].get("item") + ' picked up!')
            # delete the item from the room
            #del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        #else:
            # tell them they can't get it
            #print('no idem found')
## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        result = monsterdieroller.monsterfight()
        if result <=10:
            print('... GAME OVER!...')
            startgame = input("Would you like to start the game? (Y?N): ")
            if startgame == 'n' or startgame == 'N':
                print("Maybe next time.")
                break
            if startgame == 'y' or startgame == 'Y':
                print("Let us begin the adventure!!!!!")
                currentRoom = 'entrance'
                continue
    ## If a player enters a room with a trap
    if 'item' in rooms[currentRoom] and 'trap' in rooms[currentRoom]['item']:
        f = open(rooms[currentRoom]['story'], "r")
        txt = f.read()
        f.close()
        for char in txt:
            sleep(.05)
            sys.stdout.write(char)
        print('You are caught in a trap, and returned to the entrance')
        ## send the plyer back to the beging of the game
        currentRoom = 'entrance'
        continue