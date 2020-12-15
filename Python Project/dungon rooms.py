#dungon rooms


def showinstructions():
    # print a main menu and the commands
    print('''
Treasure Hunt Game
========
Commands:
  go [direction option's north, south, east, west]
  get [item]
========
You start from the north going south in to the cave:
''')
    print("Let us begin the adventure!!!!!")
    print()
    print("What direction would you like to go?")


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


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'entrance' : {
        'west' : 'room1',
        'south' : 'room2',
        'east' : 'room3'
        },
    'room1' :{
        'south' : 'room6',
        'item' : "trap"
        },
    'room2' : {
        'south' : 'room5',
        'item' : 'monster'
        },
    'room3' : {
        'south' : 'room4',
        },
    'room4' : {
        'west' : 'room5',
        'south' : 'room9',
        'item' : 'key'
        },
    'room5' : {
        'west' : 'room6',
        'south' : 'room8',
        'east' : 'room4'
        },
    'room6' : {
        'north' : 'room1',
        'south' : 'room7'
        },
    'room7' : {
        'north' : 'room6',
        'south' : 'room10',
        'east' : 'room8'
        },
    'room8' : {
        'west' : 'room7',
        'north' : 'room5',
        'east' : 'room9',
        'item' : 'trap'
        },
    'room9' : {
        'west' : 'room8',
        'north' : 'room4',
        'south' : 'room11',
        'item' : 'MysticalOrb'
        },
    'room10' : {
        'north' : 'room7',
        'item' : 'key'
        },
    'room11' : {
        'north' : 'room9',
        'item' : 'monster'
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

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    ## if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('no idem found')


    ## If a player enters a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('You encountered a monster... GAME OVER!')
        break

    ## If a player enters a room with a trap
    if 'item' in rooms[currentRoom] and 'trap' in rooms[currentRoom]['item']:
        print('You are caught in a trap, and returned to the entrance')
        break

    ## Define how a player can win
    if currentRoom == 'room10' and 'key' in inventory:
        print('You encountered the treasure room..... YOU WIN!')
        break
