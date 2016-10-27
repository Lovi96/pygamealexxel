def nyomtat(whichPlayer):
    for i in range(0, 10):
        if i > 0:
            print(i+1,"  ",end="")
        for o in range(0, 10):
            if i == 0 and o == 0:###############################
                print("     ",end ="")
                for p in range(0, 10):#########             #ABC
                    print(abc[p]," ",end="")
                print("\n")
                print("1   ",end="")#####################################  
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
        hilfe = 0
        for s in range(0, 10):
            if abc[s] == csoda:
                csoda = s
                hilfe = 1
        if hilfe == 1:
            valueerror=0
            return csoda
            


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
for i in range (0, 10):#                                             tömb inicializálása
    for j in range (0, 10):
        new.append(0)
    aArray.append(new)
    new = []
for i in range (0, 10):
    for j in range (0, 10):
        new.append(0)
    bArray.append(new)
    new = []


for q in range(2, 6):#                                                  a jatekos hajoi
    print("Give the positions of the {}!  ".format(shipsNames[q-2]))
    positionx = textToInt()
    positiony = int(input("Give the Y position of the {}! (1-10) ".format(shipsNames[q-2])))
    answer = input("Do you want the {} vertically? (Y/N) ".format(shipsNames[q-2]))
 
  
    for index in range(q):
        if answer == "n":
            aArray[positiony-1][index+positionx] = ships[q-2][index]
        if answer == "y":
            aArray[index+positiony-1][positionx] = ships[q-2][index]
   
    nyomtat("a")
for q in range(2, 6):#                                                  a jatekos hajoi
    print("Give the positions of the {}!  ".format(shipsNames[q-2]))
    positionx = textToInt()
    positiony = int(input("Give the Y position of the {}! (1-10) ".format(shipsNames[q-2])))
    answer = input("Do you want the {} vertically? (Y/N) ".format(shipsNames[q-2]))
  
  
    for index in range(q):
        if answer == "n":
            bArray[positiony-1][index+positionx] = ships[q-2][index]
        if answer == "y":
            bArray[index+positiony-1][positionx] = ships[q-2][index]
   
    nyomtat("b")
while True:
    shotAllready = 0
    shotPos = []
    nyomtat("aOcean")
    nyomtat("a")
    positionx = textToInt()
    positiony = int(input("hoa lősz y?: "))
    if bArray[positiony-1][positionx] == 0: 
        bArray[positiony-1][positionx] = 2
        nyomtat("aOcean")
        nyomtat("a")
    #if (bArray[positiony-1][positionx] == 3) or (bArray[positiony-1][positionx] == 4) or (bArray[positiony-1][positionx] == 5) or (bArray[positiony-1][positionx] == 6):
    if bArray[positiony-1][positionx] == 3:
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        bSubmarine -= 1
        if (bSubmarine < paSubmarine) and (bSubmarine == 0):
            print("Player 2's Submarine sank. ")
        nyomtat("a")

    elif bArray[positiony-1][positionx] == 4:
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        bCruiser -= 1
        nyomtat("a")

    elif bArray[positiony-1][positionx] == 5:
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        bMothership -= 1
        nyomtat("a")

    elif bArray[positiony-1][positionx] == 6:  
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        bBattleship -= 1
        nyomtat("a")



    nyomtat("bOcean")
    nyomtat("b")
    positionx = textToInt()
    positiony = int(input("hoa lősz y?: "))
    if aArray[positiony-1][positionx] == 0: 
        aArray[positiony-1][positionx] = 2
        nyomtat("bOcean")
        nyomtat("b")
    if (aArray[positiony-1][positionx] == 3) or (aArray[positiony-1][positionx] == 4) or (aArray[positiony-1][positionx] == 5) or (aArray[positiony-1][positionx] == 6):
        
        
        
        aArray[positiony-1][positionx] = 1
        nyomtat("bOcean")
        nyomtat("b")


    paSubmarine, pbSubmarine = aSubmarine, bSubmarine
    paCruiser, pbCruiser = aCruiser, bCruiser
    paMothership, pbMothership = aMothership, bMothership
    paBattleship, pbBattleship = aBattleship, bBattleship

