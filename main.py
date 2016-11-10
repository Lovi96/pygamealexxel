import os
import time
import random


def table_init():
    new = []
    for i in range(0, 10):  # tömbök inicializálása
        for j in range(0, 10):
            new.append(0)
        aArray.append(new)
        new = []
    for i in range(0, 10):
        for j in range(0, 10):
            new.append(0)
        bArray.append(new)
        new = []


def ai_shooting():
    global randomShooting
    while randomShooting == 1:
        xCoord = random.randint(0, 9)
        yCoord = random.randint(0, 9)
        if place_check(yCoord, xCoord, "none", 1, bArray):
            if ((bArray[yCoord][xCoord] == 3) or (bArray[yCoord][xCoord] == 4) or
                    (bArray[yCoord][xCoord] == 5) or (bArray[yCoord][xCoord] == 6)):
                bArray[yCoord][xCoord] = 1
                nyomtat(bArray)
                randomShooting = 0

            elif (bArray[yCoord][xCoord] == 0):
                bArray[yCoord][xCoord] = 2
                nyomtat(bArray)
                randomShooting = 0


def nyomtat(whichPlayer, printtype="yours"):
    for i in range(0, 10):
        if i == 9:
            print(i + 1, " ", end="")
        elif i > 0:
            print(i + 1, "  ", end="")
        for o in range(0, 10):
            if i == 0 and o == 0:
                print("     ", end="")
                for p in range(0, 10):
                    print(abc[p], " ", end="")
                print("\n")
                print("1   ", end="")
            if printtype == "yours":
                if whichPlayer[i][o] == 0:
                    print("[ ]", end="")
                if whichPlayer[i][o] == 1:
                    print("[X]", end="")
                if whichPlayer[i][o] == 2:
                    print("[O]", end="")
                if whichPlayer[i][o] == 3:
                    print("[S]", end="")
                if whichPlayer[i][o] == 4:
                    print("[C]", end="")
                if whichPlayer[i][o] == 5:
                    print("[M]", end="")
                if whichPlayer[i][o] == 6:
                    print("[B]", end="")
                if o == 9:
                    print("\n")

            if printtype == "enemy":
                if whichPlayer[i][o] in [0, 3, 4, 5, 6]:
                    print("[ ]", end="")
                if whichPlayer[i][o] == 1:
                    print("[X]", end="")
                if whichPlayer[i][o] == 2:
                    print("[O]", end="")
                if o == 9:
                    print("\n")


def textToInt():
    while True:
        input_char = input("Give the X coordinate! (A-J) ")
        if input_char == "exit":
            print("\nThe program will exit now. Bye!")
            exit()
        input_char = input_char.capitalize()
        for s in range(0, 10):
            if abc[s] == input_char:
                input_char = s
                return input_char
        else:
            print("\nNot correct char!\n")
            continue


def validInt():
    while True:
        inputint = input("Please add the Y coodrinate! (1-10) ")
        if inputint == "exit":
            print("\nThe program will exit now. Bye!")
            exit()
        if inputint == "":
            print("\nYou did not added anything\n")
            continue
        try:
            inputint = int(inputint)
            if inputint in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                return inputint
            else:
                print("\nInvalid number!\n")
                continue
        except ValueError:
            print("\nThis is not a number!\n")
            continue


def orientation():
    while True:
        inputOrientation = input("Do you want it vertically? (Y/N) ")
        if inputOrientation == "exit":
            print("\nThe program will exit now. Bye!")
            exit()
        if inputOrientation in ["y", "Y", "n", "N"]:
            inputOrientation = inputOrientation.capitalize()
            return inputOrientation
        else:
            print("\nWrong answer!\n")
            continue


def set_place(player):
    nyomtat(player)
    shipNames = ["Submarine", "Cruiser", "Mothership", "Battleship"]
    for q in range(2, 6):  # A jatekos hajoi
        while True:
            print("Give the positions of the {}!  ".format(shipNames[q - 2]))
            positionx = textToInt()
            positiony = validInt() - 1
            answer = orientation()
            if place_check(positiony, positionx, answer, q, player):
                for index in range(q):
                    if answer == "N":
                        player[positiony][index + positionx] = ships[q - 2][index]
                    if answer == "Y":
                        player[index + positiony][positionx] = ships[q - 2][index]
                break
            else:
                print("\nInvalid position!!\n")
                continue
        nyomtat(player)


def place_check(y, x, orientation, lenght, player):
    """Checks the places. If the place is out of the table, or contains ships, return False."""

    problem = 0
    if orientation == "none":  # SIMAPEW
        if (x > 9) or (y > 9) or (player[y][x] in [1, 2]):
            problem = 1

    if orientation == "Y":  # LEFELE
        for i in range(lenght):
            if (x > 9) or ((i + y) > 9) or (player[y + i][x] in [1, 2, 3, 4, 5, 6]):
                problem = 1

    if orientation == "N":  # OLDALRAFELE
        for i in range(lenght):
            if ((i + x) > 9) or (y > 9) or (player[y][x + i] in [1, 2, 3, 4, 5, 6]):
                problem = 1
    if problem == 1:
        return False
    else:
        return True


def pew(player):
    array = []
    self_Array = []
    global aSubmarine, bSubmarine, aCruiser, bCruiser, aMothership, bMothership, aBattleship, bBattleship
    global paSubmarine, pbSubmarine, paCruiser, pbCruiser, paMothership, pbMothership, paBattleship, pbBattleship
    global aArray, bArray
    Submarine, Cruiser, Mothership, Battleship, pSubmarine, pCruiser, pMothership, pBattleship = 0, 0, 0, 0, 0, 0, 0, 0
    if player == "Player 2":
        array = aArray
        self_Array = bArray
        Submarine, Cruiser, Mothership, Battleship = aSubmarine, aCruiser, aMothership, aBattleship
        pSubmarine, pCruiser, pMothership, pBattleship = paSubmarine, paCruiser, paMothership, paBattleship
    if player == "Player 1":
        array = bArray
        self_Array = aArray
        Submarine, Cruiser, Mothership, Battleship = bSubmarine, bCruiser, bMothership, bBattleship
        Submarine, Cruiser, Mothership, Battleship = pbSubmarine, pbCruiser, pbMothership, pbBattleship
    nyomtat(self_Array)
    print("      ↑↑↑↑↑↑↑ Your table ↑↑↑↑↑↑↑\n      ↓↓↓↓↓↓↓ Enemy table↓↓↓↓↓↓↓")  # cucccccccccccccccccccccccccc
    print("fent a tiéd, lent az ellenfélé")
    nyomtat(array, "enemy")
    while True:
        print("This is your turn, ", player, ". Take your shoot! ")
        positionx = textToInt()
        positiony = validInt() - 1
        if place_check(positiony, positionx, "none", 1, array):
            if array[positiony][positionx] == 0:
                array[positiony][positionx] = 2
                nyomtat(array, "enemy")
                print("MISS")

            if array[positiony][positionx] == 3:
                array[positiony][positionx] = 1
                nyomtat(array, "enemy")
                Submarine -= 1
                if (Submarine < pSubmarine) and (Submarine == 0):
                    print(player, "'s Submarine sank. ")
                pSubmarine = Submarine
                print("BÄMM")

            elif array[positiony][positionx] == 4:
                array[positiony][positionx] = 1
                nyomtat(array, "enemy")
                Cruiser -= 1
                if (Cruiser < pCruiser) and (Cruiser == 0):
                    print(player, "'s Cruiser sank. ")
                pCruiser = Cruiser
                print("BÄMM")

            elif array[positiony][positionx] == 5:
                array[positiony][positionx] = 1
                nyomtat(array, "enemy")
                Mothership -= 1
                if (Mothership < pMothership) and (Mothership == 0):
                    print(player, "'s Mothership sank. ")
                pMothership = Mothership
                print("BÄMM")

            elif array[positiony][positionx] == 6:
                array[positiony][positionx] = 1
                nyomtat(array, "enemy")
                Battleship -= 1
                if (Battleship < pBattleship) and (Battleship == 0):
                    print(player, "'s Battleship sank. ")
                pBattleship = Battleship
                print("BÄMM")

            if player == "Player 2":
                aSubmarine, aCruiser, aMothership, aBattleship = Submarine, Cruiser, Mothership, Battleship
                paSubmarine, paCruiser, paMothership, paBattleship = pSubmarine, pCruiser, pMothership, pBattleship
            if player == "Player 1":
                bSubmarine, bCruiser, bMothership, bBattleship = Submarine, Cruiser, Mothership, Battleship
                pbSubmarine, pbCruiser, pbMothership, pbBattleship = Submarine, Cruiser, Mothership, Battleship

            break
        else:
            ("Invalid location! Try again! ")
            continue
    playerSwitch()


def playerSwitch():
    input("Press enter if you done ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Switching players!")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print('\n' * 10)


def check_win():
    if (aSubmarine == 0) and (aBattleship == 0) and (aMothership == 0) and (aCruiser == 0):
        print("\n\nPLAYER 2 WINS!!!" * 3)
        exit()
    if (bSubmarine == 0) and (bBattleship == 0) and (bMothership == 0) and (bCruiser == 0):
        print("\n\nPLAYER 1 WINS!!!" * 3)
        exit()


def PVP():
    input("\nNow, you will place the ships. Player 1 starts first.\nPress enter to continue\n")
    table_init()
    set_place(aArray)
    playerSwitch()
    input("\nNow player 2 place their ships.\n")
    set_place(bArray)
    while True:
        pew("Player 1")
        check_win()
        pew("Player 2")
        check_win()


def PVE():
    print("Place your ships!")
    table_init()
    set_place(aArray)
    ai_ship_placement()
    while True:
        global randomShooting
        pew(aArray)
        randomShooting = 1
        check_win
        # to be continued


def ai_ship_placement():
    for q in range(2, 6):
        while True:
            xCoord = random.randint(0, 9)
            yCoord = random.randint(0, 9)
            verticalPlacement = random.randint(0, 1)
            if verticalPlacement == 0:
                verticalPlacement = "N"
            if verticalPlacement == 1:
                verticalPlacement = "Y"
            if place_check(yCoord, xCoord, verticalPlacement, q, bArray):
                for index in range(q):
                    if verticalPlacement == "N":
                        bArray[yCoord][index + xCoord] = ships[q - 2][index]
                    if verticalPlacement == "Y":
                        bArray[index + yCoord][xCoord] = ships[q - 2][index]
            else:
                continue
            break
    nyomtat(bArray)


aArray = []
bArray = []
fivelengthship = [6, 6, 6, 6, 6]
fourlengthship = [5, 5, 5, 5]
threelengthship = [4, 4, 4]
twolengthship = [3, 3]

aSubmarine, bSubmarine = 2, 2
aCruiser, bCruiser = 3, 3
aMothership, bMothership = 4, 4
aBattleship, bBattleship = 5, 5

paSubmarine, pbSubmarine = 2, 2
paCruiser, pbCruiser = 3, 3
paMothership, pbMothership = 4, 4
paBattleship, pbBattleship = 5, 5


ships = [twolengthship, threelengthship, fourlengthship, fivelengthship]
shipNames = ["Submarine", "Cruiser", "Mothership", "Battleship"]
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# ez itt a main

print("Welcome to our game!\n\nYou can choose between two game type:\nPress P for the PVP (play against real player) or")
print('Press E for the PVE (play against the computer)\n\nRemember, you can always quit, if you type "exit"\nHave fun :)')
while True:
    gametype = input()
    if gametype in ["p", "P", "pvp", "PVP", "1"]:
        PVP()
    elif gametype in ["e", "E", "pve", "PVE", "2"]:
        print("bocsesz, ez még készülőben van")
    elif gametype == "exit":
        print("\nThe program will exit now. Bye!")
        exit()
    else:
        continue


"""" debug tools :D

aArray = [[3, 4, 5, 6, 0, 0, 0, 0, 0, 0],
          [3, 4, 5, 6, 0, 0, 0, 0, 0, 0],
          [0, 4, 5, 6, 0, 0, 0, 0, 0, 0],
          [0, 0, 5, 6, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

bArray = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 6, 6, 6, 6, 6],
          [0, 0, 0, 0, 0, 0, 5, 5, 5, 5],
          [0, 0, 0, 0, 0, 0, 0, 4, 4, 4],
          [0, 0, 0, 0, 0, 0, 0, 0, 3, 3]]

set_place(aArray)
set_place(bArray)
ai_ship_placement()

 player 1
nyomtat(bArray)
set_place(bArray)
nyomtat(bArray)
playerSwitch()
pew()
"""
