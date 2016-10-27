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
        if answer == "N":
            aArray[positiony-1][index+positionx] = ships[q-2][index]
        if answer == "Y":
            aArray[index+positiony-1][positionx] = ships[q-2][index]
   
    nyomtat("a")
for q in range(2, 6):#                                                  a jatekos hajoi
    print("Give the positions of the {}!  ".format(shipsNames[q-2]))
    positionx = textToInt()
    positiony = int(input("Give the Y position of the {}! (1-10) ".format(shipsNames[q-2])))
    answer = input("Do you want the {} vertically? (Y/N) ".format(shipsNames[q-2]))
  
  
    for index in range(q):
        if answer == "N":
            bArray[positiony-1][index+positionx] = ships[q-2][index]
        if answer == "Y":
            bArray[index+positiony-1][positionx] = ships[q-2][index]
   
    nyomtat("b")
while True:
    nyomtat("aOcean")
    nyomtat("a")
    print("\n\nPlayer 1: Where would you like to shoot?")
    positionx = textToInt()
    positiony = int(input("Give the Y coordinate! (A-J) "))
    if bArray[positiony-1][positionx] == 0: 
        bArray[positiony-1][positionx] = 2
        nyomtat("aOcean")
        nyomtat("a")
    if (bArray[positiony-1][positionx] == 3) or (bArray[positiony-1][positionx] == 4) or (bArray[positiony-1][positionx] == 5) or (bArray[positiony-1][positionx] == 6):
        bArray[positiony-1][positionx] = 1
        nyomtat("aOcean")
        nyomtat("a")
    nyomtat("bOcean")
    nyomtat("b")
    print("\n\nPlayer 2: Where would you like to shoot?")
    positionx = textToInt()
    positiony = int(input("Give the Y coordinate! (A-J) "))
    if aArray[positiony-1][positionx] == 0: 
        aArray[positiony-1][positionx] = 2
        nyomtat("bOcean")
        nyomtat("b")
    if (aArray[positiony-1][positionx] == 3) or (aArray[positiony-1][positionx] == 4) or (aArray[positiony-1][positionx] == 5) or (aArray[positiony-1][positionx] == 6):
        aArray[positiony-1][positionx] = 1
        nyomtat("bOcean")
        nyomtat("b")




