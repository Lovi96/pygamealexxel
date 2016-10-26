def nyomtat(whichPlayer):
    for i in range(0, 10):#                            a kiíratás 
        for o in range(0, 10):
            if whichPlayer == "a":
                if aArray[i][o] == 0:
                    print("[ ]",end="")
                if aArray[i][o] == 1:
                    print("[X]",end="")
                if aArray[i][o] == 2:
                    print("[O]",end="")
                if aArray[i][o] == 3:
                    print("[#]",end="")
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
                    print("[#]",end="")
                if o == 9:
                    print("\n")

aArray = []
bArray = []

fivelengthship = [3,3,3,3,3]
fourlengthship = [3,3,3,3]
threelengthship = [3,3,3]
twolengthship = [3,3]

ships = [twolengthship, threelengthship, fourlengthship, fivelengthship]

new = []
for i in range (0, 10):#                         tömb inicializálása
    for j in range (0, 10):
        new.append(0)
    aArray.append(new)
    new = []
for i in range (0, 10):
    for j in range (0, 10):
        new.append(0)
    bArray.append(new)
    new = []


for q in range(2, 6):
    positionx = int(input("adjad meg a x {} pozitronÁT!".format(q)))
    positiony = int(input("adjad meg a y {} pozitronÁT!".format(q)))
    answer = input("föggőleges legyene a {} hossz hajó y/n".format(q))  
  
    for index in range(q):
        if answer == "n":
            aArray[positiony-1][index+positionx-1] = fivelengthship[q-2]
        if answer == "y":
            aArray[index+positiony-1][positionx-1] = fivelengthship[q-2]
   
    nyomtat("a")





