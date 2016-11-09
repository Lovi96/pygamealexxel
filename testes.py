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
    if orientation == "Y":      #LEFELE
        for i in range(lenght):
            if (x>9) or ((i+y)>9) or (player[y+i][x] in [3, 4, 5, 6]):
                problem = 1
                
    if orientation == "N":      #OLDALRAFELE
        for i in range(lenght):
            if ((i+x)>9) or (y>9)  or (player[y][x+i] in [3, 4, 5, 6]):
                problem = 1
    if problem == 1:
        return False
    else:
        return True

def set_place(player):
    shipsNames = ["Submarine", "Cruiser", "Mothership", "Battleship"]
    for q in range(2, 6):  # A jatekos hajoi
        while True:

            print("Give the positions of the {}!  ".format(shipsNames[q - 2]))
            positionx = textToInt()        
            positiony = int(input("Give the Y position of the {}! (1-10) ".format(shipsNames[q - 2])))
            positiony -= 1
            answer = input("Do you want the {} vertically? (Y/N) ".format(shipsNames[q - 2])).capitalize()
            if place_check(positiony, positionx, answer, q, player):
                for index in range(q):
                    if answer == "N":
                        player[positiony][index + positionx] = ships[q - 2][index]
                    if answer == "Y":
                        player[index + positiony][positionx] = ships[q - 2][index]
            else:
                print("invalid position!!")
                continue

        nyomtat(player)
ships = [twolengthship, threelengthship, fourlengthship, fivelengthship]
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
shipsNames = ["Submarine", "Cruiser", "Mothership", "Battleship"]
fivelengthship = [6, 6, 6, 6, 6]
fourlengthship = [5, 5, 5, 5]
threelengthship = [4, 4, 4]
twolengthship = [3, 3]
aArray = [[4,4,4,4,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,4,0,0,0,0,4],
          [0,0,0,0,4,0,0,0,0,4],
          [0,0,0,0,4,0,0,0,0,4],
          [0,0,0,0,4,0,0,0,0,4],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,4,4,4,4,4]]

set_place(aArray)
print("végem :)\n")