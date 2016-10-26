def nyomtat(whichPlayer):
    for i in range(0, 10):
        if i > 0:
            print(i+1,"  ",end="")
        for o in range(0, 10):
            if i == 0 and o == 0:###############################
                print("     ",end ="")
                for p in range(0, 10):#########             #ABC
                    print(abc[p]," ",end="")
                print("\n")#####################################
            if i==0 and o==0:
                print("1   ",end="")
            if whichPlayer == "a":
                if aArray[i][o] == 0:
                    print("[ ]",end="")
                if aArray[i][o] == 1:
                    print("[X]",end="")
                if aArray[i][o] == 2:
                    print("[O]",end="")
                if aArray[i][o] == 3:
                    print("[T]",end="")
                if aArray[i][o] == 4:
                    print("[C]",end="")
                if aArray[i][o] == 5:
                    print("[A]",end="")
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
                    print("[#]",end="")
                if o == 9:
                    print("\n")

aArray = []
bArray = []
prInt = 0   #ddddddddddddddddddddddddsadasdéjfalwejflwefkkláaweefkáéfkáélwekfwkáéwaockwarlock
fivelengthship = [6,6,6,6,6]
fourlengthship = [5,5,5,5]
threelengthship = [4,4,4]
twolengthship = [3,3]

ships = [twolengthship, threelengthship, fourlengthship, fivelengthship]

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
    positionx = int(input("adjad meg a x {} pozitronÁT!".format(q)))
    positiony = int(input("adjad meg a y {} pozitronÁT!".format(q)))
    answer = input("föggőleges legyene a {} hossz hajó y/n".format(q))  
  
    for index in range(q):
        if answer == "n":
            aArray[positiony-1][index+positionx-1] = ships[q-2][index]
        if answer == "y":
            aArray[index+positiony-1][positionx-1] = ships[q-2][index]
   
    nyomtat("a")
while True:
    shotAllready = 0
    shotPos = []
    positionx = int(input("Hova lösz x : "))
    positiony = int(input("hoa lősz y?: "))
    if aArray[positiony-1][positionx-1] == 0: 
        aArray[positiony-1][positionx-1] = 2
        nyomtat("a")
        break
    if aArray[positiony-1][positionx-1] != 0:
        aArray[positiony-1][positionx-1] = 1
        nyomtat("a")
        break




