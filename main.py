aArray = []
bArray = []

fivelengthship = [3,3,3,3,3]


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

aArray[2][2] = 3
bArray[3][3] = 3

positionx = int(input("adjad meg az x pozitront!"))
positiony = int(input("adjad meg az y pozitront!"))
ansver = input("föggőleges legyene?  y/n")
if ansver == "n":
    for q in range(len(fivelengthship)):
        aArray[positiony-1][q+positionx-1] = fivelengthship[q]
if ansver == "y":
    for q in range(len(fivelengthship)):
        aArray[q+positiony-1][positionx-1] = fivelengthship[q]


for i in range(0, 10):#                            a kiíratás
    for o in range(0, 10):
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










