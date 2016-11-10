import random
# from main import *


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
    valueerror = 1
    while valueerror == 1:
        csoda = input("Give the X coordinate! (A-J) ")
        csoda = csoda.capitalize()
        hilfe = 0
        for s in range(0, 10):
            if abc[s] == csoda:
                csoda = s
                hilfe = 1
        if hilfe == 1:
            valueerror = 0
            return csoda


def place_check(y, x, orientation, lenght, player):
    """Checks the places. If the place is out of the table, or contains ships, return False."""

    problem = 0
    if orientation == "none":  # SIMAPEW
        if (x > 9) or (y > 9) or (y < 0) or (x < 0) or (player[y][x] in [1, 2]):
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
            if place_check(yCoord, xCoord, verticalPlacement, q, aArray):
                for index in range(q):
                    if verticalPlacement == "N":
                        aArray[yCoord][index + xCoord] = ships[q - 2][index]
                    if verticalPlacement == "Y":
                        aArray[index + yCoord][xCoord] = ships[q - 2][index]
            else:
                continue
            break
    nyomtat(aArray)

move = 0


def artificial_intelligence():
    global move
    input("\ncsapassad\n")
    if aiVar == 2:
        bombardment()
    elif aiVar == 1:
        pos_checker()
    elif aiVar == 0:
        random_shooting()
    move += 1
    print(move)


def random_shooting():
    global yCoord, xCoord, aiVar
    while True:
        xCoord = random.randint(0, 9)
        yCoord = random.randint(0, 9)
        if place_check(yCoord, xCoord, "none", 1, aArray):
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1

                aiVar = 1

            elif (aArray[yCoord][xCoord] == 0):
                aArray[yCoord][xCoord] = 2

                aiVar = 0
            break
    nyomtat(aArray)


def pos_checker():
    global yCoord, xCoord, aiVar, shootDir, yPoschecker, xPoschecker
    if shootDir == 0:
        if place_check(yCoord - 1, xCoord, "none", 1, aArray):
            if aArray[yCoord - 1][xCoord] in [3, 4, 5, 6]:
                aArray[yCoord - 1][xCoord] = 1
                yPoschecker, xPoschecker = yCoord - 1, xCoord
                aiVar = 2
            else:
                aArray[yCoord - 1][xCoord] = 2
                shootDir = 1
        else:
            shootDir = 1
    if shootDir == 1:
        if place_check(yCoord, xCoord + 1, "none", 1, aArray):
            if aArray[yCoord][xCoord + 1] in [3, 4, 5, 6]:
                aArray[yCoord][xCoord + 1] = 1
                yPoschecker, xPoschecker = yCoord, xCoord + 1
                aiVar = 2
            else:
                aArray[yCoord][xCoord + 1] = 2
                shootDir = 2
        else:
            shootDir = 2
    if shootDir == 2:
        if place_check(yCoord + 1, xCoord, "none", 1, aArray):
            if aArray[yCoord + 1][xCoord] in [3, 4, 5, 6]:
                aArray[yCoord + 1][xCoord] = 1
                yPoschecker, xPoschecker = yCoord + 1, xCoord
                aiVar = 2
            else:
                aArray[yCoord + 1][xCoord] = 2
                shootDir = 3
        else:
            shootDir = 3
    if shootDir == 3:
        if place_check(yCoord, xCoord - 1, "none", 1, aArray):
            if aArray[yCoord][xCoord - 1] in [3, 4, 5, 6]:
                aArray[yCoord][xCoord - 1] = 1
                yPoschecker, xPoschecker = yCoord, xCoord - 1
                aiVar = 2
            else:
                aArray[yCoord][xCoord - 1] = 2
                shootDir = 0
                aiVar = 0
        else:
            shootDir = 0
            aiVar = 0
    else:
        aiVar = 0
    nyomtat(aArray)


def bombardment():
    global yCoord, xCoord, aiVar, shootDir, yPoschecker, xPoschecker, yBombardment, xBombardment
    if shootDir == 0:
        if place_check(yPoschecker - 1, xPoschecker, "none", 1, aArray):
            if aArray[yPoschecker - 1][xPoschecker] in [3, 4, 5, 6]:
                aArray[yPoschecker - 1][xPoschecker] = 1
                yPoschecker, xPoschecker = yPoschecker - 1, xPoschecker
            else:
                aArray[yPoschecker - 1][xPoschecker] = 2
                aiVar = 1
                shootDir = 2
        else:
            aiVar = 1
            shootDir = 2

    elif shootDir == 1:
        if place_check(yPoschecker, xPoschecker + 1, "none", 1, aArray):
            if aArray[yPoschecker][xPoschecker + 1] in [3, 4, 5, 6]:
                aArray[yPoschecker][xPoschecker + 1] = 1
                yPoschecker, xPoschecker = yPoschecker, xPoschecker + 1
            else:
                aArray[yPoschecker][xPoschecker + 1] = 2
                aiVar = 1
                shootDir = 3
        else:
            aiVar = 1
            shootDir = 3

    elif shootDir == 2:
        if place_check(yPoschecker + 1, xPoschecker, "none", 1, aArray):
            if aArray[yPoschecker + 1][xPoschecker] in [3, 4, 5, 6]:
                aArray[yPoschecker + 1][xPoschecker] = 1
                yPoschecker, xPoschecker = yPoschecker + 1, xPoschecker
            else:
                aArray[yPoschecker + 1][xPoschecker] = 2
                aiVar = 1
                shootDir = 0
        else:
            aiVar = 1
            shootDir = 0

    elif shootDir == 3:
        if place_check(yPoschecker, xPoschecker - 1, "none", 1, aArray):
            if aArray[yPoschecker][xPoschecker - 1] in [3, 4, 5, 6]:
                aArray[yPoschecker][xPoschecker - 1] = 1
                yPoschecker, xPoschecker = yPoschecker, xPoschecker - 1
            else:
                aArray[yPoschecker][xPoschecker - 1] = 2
                aiVar = 1
                shootDir = 1
        else:
            aiVar = 1
            shootDir = 1
    nyomtat(aArray)


yCoord = 0
xCoord = 0
yPoschecker = 0
xPoschecker = 0
aiVar = 0
shootDir = 0
yBombardment = 0
xBombardment = 0


aArray = []
fivelengthship = [6, 6, 6, 6, 6]
fourlengthship = [5, 5, 5, 5]
threelengthship = [4, 4, 4]
twolengthship = [3, 3]

ships = [twolengthship, threelengthship, fourlengthship, fivelengthship]
shipsNames = ["Submarine", "Cruiser", "Mothership", "Battleship"]
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
new = []
for i in range(0, 10):
    for j in range(0, 10):
        new.append(0)
    aArray.append(new)
    new = []
ai_ship_placement()
while True:
    artificial_intelligence()
