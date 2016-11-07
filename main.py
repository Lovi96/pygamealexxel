import os
import time

def nyomtat(whichPlayer):
    for i in range(0, 10):
        if i == 9:
            print(i+1," ",end="")
        elif i > 0:
            print(i+1,"  ",end="")
        for o in range(0, 10):
            if i == 0 and o == 0:
                print("     ",end ="")
                for p in range(0, 10):
                    print(abc[p]," ",end="")
                print("\n")
                print("1   ",end="")
            if whichPlayer == "a":
                if aArray[i][o] == 0:
                    print("[ ]",end="")
                if aArray[i][o] == 1:
                    print("[X]",end="")
                if aArray[i][o] == 2:
                    print("[O]",end="")
                if aArray[i][o] == 3:
                    print("[S]",end="")
                if aArray[i][o] == 4:
                    print("[C]",end="")
                if aArray[i][o] == 5:
                    print("[M]",end="")
                if aArray[i][o] == 6:
                    print("[B]",end="")
                if o == 9:
                    print("\n")

            if whichPlayer == "b":
                if bArray[i][o] == 0:
                    print("[ ]",end="")
                if bArray[i][o] == 1:
                    print("[X]",end="")
                if bArray[i][o] == 2:
                    print("[O]",end="")
                if bArray[i][o] == 3:
                    print("[S]",end="")
                if bArray[i][o] == 4:
                    print("[C]",end="")
                if bArray[i][o] == 5:
                    print("[M]",end="")
                if bArray[i][o] == 6:
                    print("[B]",end="")
                if o == 9:
                    print("\n")

            if whichPlayer == "aOcean":
                if bArray[i][o] == 0:
                    print("[ ]",end="")
                if bArray[i][o] == 1:
                    print("[X]",end="")
                if bArray[i][o] == 2:
                    print("[O]",end="")
                if bArray[i][o] == 3:
                    print("[ ]",end="")
                if bArray[i][o] == 4:
                    print("[ ]",end="")
                if bArray[i][o] == 5:
                    print("[ ]",end="")
                if bArray[i][o] == 6:
                    print("[ ]",end="")
                if o == 9:
                    print("\n")

            if whichPlayer == "bOcean":
                if aArray[i][o] == 0:
                    print("[ ]",end="")
                if aArray[i][o] == 1:
                    print("[X]",end="")
                if aArray[i][o] == 2:
                    print("[O]",end="")
                if aArray[i][o] == 3:
                    print("[ ]",end="")
                if aArray[i][o] == 4:
                    print("[ ]",end="")
                if aArray[i][o] == 5:
                    print("[ ]",end="")
                if aArray[i][o] == 6:
                    print("[ ]",end="")
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
            valueerror=0
            return csoda

def playerSwitch():
    print("Switching players!")
    for i in range(5,0,-1):
        print(i)
        time.sleep(1)
    print('\n' * 50)
    os.system('cls' if os.name=='nt' else 'clear')

           
aArray = []
bArray = []
fivelengthship = [6,6,6,6,6]
fourlengthship = [5,5,5,5]
threelengthship = [4,4,4]
twolengthship = [3,3]

aSubmarine, bSubmarine = 2, 2
aCruiser, bCruiser = 3, 3
aMothership, bMothership = 4, 4
aBattleship, bBattleship = 5, 5

paSubmarine, pbSubmarine = 2, 2
paCruiser, pbCruiser = 3, 3
paMothership, pbMothership = 4, 4
paBattleship, pbBattleship = 5, 5


ships = [twolengthship, threelengthship, fourlengthship, fivelengthship]
shipsNames = ["Submarine", "Cruiser", "Mothership", "Battleship"]
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

new = []
for i in range (0, 10):#                                             tömbök inicializálása
    for j in range (0, 10):
        new.append(0)
    aArray.append(new)
    new = []
for i in range (0, 10):
    for j in range (0, 10):
        new.append(0)
    bArray.append(new)
    new = []

nyomtat("a")
for q in range(2, 6):#                                                  A jatekos hajoi
    print("Give the positions of the {}!  ".format(shipsNames[q-2]))
    positionx = textToInt()
    positiony = int(input("Give the Y position of the {}! (1-10) ".format(shipsNames[q-2])))
    answer = input("Do you want the {} vertically? (Y/N) ".format(shipsNames[q-2]))
    answer = answer.capitalize()
 
    for index in range(q):
        if answer == "N":
            aArray[positiony-1][index+positionx] = ships[q-2][index]
        if answer == "Y":
            aArray[index+positiony-1][positionx] = ships[q-2][index]
    nyomtat("a")
playerSwitch()
nyomtat("b")
for q in range(2, 6):#                                                  B jatekos hajoi
    print("Give the positions of the {}!  ".format(shipsNames[q-2]))
    positionx = textToInt()
    positiony = int(input("Give the Y position of the {}! (1-10) ".format(shipsNames[q-2])))
    answer = input("Do you want the {} vertically? (Y/N) ".format(shipsNames[q-2]))
    answer = answer.capitalize()
  
    for index in range(q):
        if answer == "N":
            bArray[positiony-1][index+positionx] = ships[q-2][index]
        if answer == "Y":
            bArray[index+positiony-1][positionx] = ships[q-2][index]
    nyomtat("b")
playerSwitch()
while True:#                                                             PEW PEW
    if (aSubmarine == 0) and (aBattleship == 0) and (aMothership == 0) and (aCruiser == 0):
        print("\n\nPLAYER 2 WINS!!!"*3)
        break
    if (bSubmarine == 0) and (bBattleship == 0) and (bMothership == 0) and (bCruiser == 0):
        print("\n\nPLAYER 1 WINS!!!"*3)
        break
    nyomtat("a")
    print("      ↑↑↑↑↑↑↑ Your table ↑↑↑↑↑↑↑\n      ↓↓↓↓↓↓↓ Enemy table↓↓↓↓↓↓↓")
    nyomtat("aOcean")
    print("\n\nPlayer 1: Where would you like to shoot?")
    positionx = textToInt()
    positiony = int(input("Give the Y coordinate! (1-10) "))
    if bArray[positiony-1][positionx] == 0: 
        bArray[positiony-1][positionx] = 2
        nyomtat("aOcean")
        print("MISS")
    
    if bArray[positiony-1][positionx] == 3:
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        bSubmarine -= 1
        if (bSubmarine < pbSubmarine) and (bSubmarine == 0):
            print("Player 2's Submarine sank. ")
        pbSubmarine = bSubmarine
        print("BÄMM")

    elif bArray[positiony-1][positionx] == 4:
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        bCruiser -= 1
        if (bCruiser < pbCruiser) and (bCruiser == 0):
            print("Player 2's Cruiser sank. ")
        pbCruiser = bCruiser
        print("BÄMM")      

    elif bArray[positiony-1][positionx] == 5:
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        bMothership -= 1
        if (bMothership < pbMothership) and (bMothership == 0):
            print("Player 2's Mothership sank. ")
        pbMothership = bMothership 
        print("BÄMM") 

    elif bArray[positiony-1][positionx] == 6:  
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        bBattleship -= 1
        if (bBattleship < pbBattleship) and (bBattleship == 0):
            print("Player 2's Battleship sank. ")
        pbBattleship = bBattleship 
        print("BÄMM")
    playerSwitch()

    nyomtat("b")
    print("      ↑↑↑↑↑↑↑ Your table ↑↑↑↑↑↑↑\n      ↓↓↓↓↓↓↓ Enemy table↓↓↓↓↓↓↓")
    nyomtat("bOcean")
    print("\n\nPlayer 2: Where would you like to shoot?")
    positionx = textToInt()
    positiony = int(input("Give the Y coordinate! (1-10) "))
    if aArray[positiony-1][positionx] == 0: 
        aArray[positiony-1][positionx] = 2
        nyomtat("bOcean")
        print("miss")
        
    if aArray[positiony-1][positionx] == 3:
        aArray[positiony-1][positionx] = 1
        nyomtat("bOcean")
        aSubmarine -= 1
        if (aSubmarine < paSubmarine) and (aSubmarine == 0):
            print("Player 1's Submarine sank. ")
        paSubmarine = aSubmarine
        print("BÄMM")

    elif aArray[positiony-1][positionx] == 4:
        aArray[positiony-1][positionx] = 1
        nyomtat("bOcean")
        aCruiser -= 1
        if (aCruiser < paCruiser) and (aCruiser == 0):
            print("Player 1's Cruiser sank. ")
        paCruiser = aCruiser 
        print("BÄMM ")     

    elif aArray[positiony-1][positionx] == 5:
        aArray[positiony-1][positionx] = 1
        nyomtat("bOcean")
        aMothership -= 1
        if (aMothership < paMothership) and (aMothership == 0):
            print("Player 1's Mothership sank. ")
        paMothership = aMothership  
        print("BÄMM")

    elif aArray[positiony-1][positionx] == 6:  
        aArray[positiony-1][positionx] = 1
        nyomtat("bOcean")
        aBattleship -= 1
        if (aBattleship < paBattleship) and (aBattleship == 0):
            print("Player 1's Battleship sank. ")
        paBattleship = aBattleship 
        print("BÄMM")
    playerSwitch()
