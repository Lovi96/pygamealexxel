def nyomtat():
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


positionx = int(input("adjad meg az x pozitront!"))
positiony = int(input("adjad meg az y pozitront!"))
ansver = input("föggőleges legyene?  y/n")



for w in ships:
    index = 2
    positionx = int(input("adjad meg a"+w+" x pozitronÁT!"))
    positiony = int(input("adjad meg az"+w+" y pozitront!"))
    ansver = input("föggőleges legyene?  y/n \n")

    if ansver == "n":
        for index in range(len(fivelengthship)):
            aArray[positiony-1][index+positionx-1] = fivelengthship[q]
    if ansver == "y":
        for index in range(len(fivelengthship)):
            aArray[index+positiony-1][positionx-1] = fivelengthship[q]
    nyomtat()
    index += 1
















