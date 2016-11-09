import random
# from main import *

randomShooting = 1

setBombardment = 0
shootDir = 1


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
    if orientation == "Y":  # LEFELE
        for i in range(lenght):
            if (x > 9) or ((i + y) > 9) or (player[y + i][x] in [3, 4, 5, 6]):
                problem = 1

    if orientation == "N":  # OLDALRAFELE
        for i in range(lenght):

            if ((i + x) > 9) or (y > 9) or (player[y][x + i] in [3, 4, 5, 6]):
                problem = 1
    if problem == 1:
        return False
    else:
        return True


def bombardment(coords2):
    print(coords2)
    global aArray
    print(shootDir)
    global setBombardment
    global randomShooting
    yCoord = coords2[0]
    xCoord = coords2[1]
    while randomShooting == 0 and setBombardment == 1:
        if (shootDir == 1):
            yCoord -= 1
            nyomtat(aArray)
            if (aArray[yCoord][xCoord] == 3):
                aArray[yCoord][xCoord] = 1
                break

        elif (shootDir == 2):
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1
                xCoord += 1
                break

        elif (shootDir == 3):
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1
                yCoord -= 1
                break

        elif (shootDir == 4):
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1
                xCoord -= 1
                break


def pos_checker(coords):
    global randomShooting
    global shootDir
    yCoord = coords[0]
    print(shootDir)
    print(yCoord)
    xCoord = coords[1]
    print(xCoord)
    # randomShooting = 0
    global setBombardment
    while randomShooting == 0 and setBombardment == 0:
        if (shootDir == 1):
            yCoord -= 1
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1
                setBombardment = 1
                return yCoord, xCoord

            elif (aArray[yCoord][xCoord] == 0):
                aArray[yCoord][xCoord] = 2
                shootDir += 1
                return yCoord, xCoord

        elif (shootDir == 2):
            xCoord += 1
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1
                setBombardment = 1
                return yCoord, xCoord

            else:
                aArray[yCoord][xCoord] = 2
                shootDir += 1
                return yCoord, xCoord

        elif (shootDir == 3):
            yCoord += 1
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1
                setBombardment = 1
                return yCoord, xCoord

            else:
                aArray[yCoord][xCoord] = 2
                shootDir += 1
                return yCoord, xCoord

        elif (shootDir == 4):
            xCoord -= 1
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1
                setBombardment = 1
                return yCoord, xCoord
            elif (aArray[yCoord][xCoord] == 0):
                aArray[yCoord][xCoord] = 2
                return yCoord, xCoord

        shootDir = 1
        randomShooting = 1
        break


def ai_shooting():
    global randomShooting
    while randomShooting == 1:
        xCoord = random.randint(0, 9)
        yCoord = random.randint(0, 9)
        if place_check(yCoord, xCoord, "none", 1, aArray):
            if ((aArray[yCoord][xCoord] == 3) or (aArray[yCoord][xCoord] == 4) or
                    (aArray[yCoord][xCoord] == 5) or (aArray[yCoord][xCoord] == 6)):
                aArray[yCoord][xCoord] = 1
                nyomtat(aArray)
                randomShooting = 0
                return yCoord, xCoord

            elif (aArray[yCoord][xCoord] == 0):
                aArray[yCoord][xCoord] = 2


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

aArray = []
fivelengthship = [6, 6, 6, 6, 6]
fourlengthship = [5, 5, 5, 5]
threelengthship = [4, 4, 4]
twolengthship = [3, 3]
xCoord = 1
yCoord = 1

ships = [twolengthship, threelengthship, fourlengthship, fivelengthship]
shipsNames = ["Submarine", "Cruiser", "Mothership", "Battleship"]
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
new = []
for i in range(0, 10):
    for j in range(0, 10):
        new.append(0)
    aArray.append(new)
    new = []
randomShooting = 1
# set_place(aArray)
ai_ship_placement()
"""print(type(ai_shooting()))
print(ai_shooting())
pos_checker(ai_shooting())"""
while True:
    bombardment(pos_checker(ai_shooting()))
# while True:

#    ai_shooting()
#    nyomtat(bArray, "enemy")
