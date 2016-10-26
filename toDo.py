import pickle
while True:
    try:
        thelist = pickle.load(open("list.py", "r+b"))
        marklist = pickle.load(open("marklist.py", "r+b"))
    except EOFError:
        thelist = []
        anadalist = []
        marklist = []
        toAdd = str(input("What would you like  to add? \n"))
        thelist.append(toAdd)
        marklist.append(False)
        pickle.dump(marklist, open("marklist.py", "r+b")) 
        pickle.dump(thelist, open("list.py", "r+b"))
    thelist = []
    anadalist = []
    marklist = []
    operation = str(input("What would you like to do?\n"))
    thelist = pickle.load(open("list.py", "r+b"))
    marklist = pickle.load(open("marklist.py", "r+b"))
    if operation == "x":
        break
    if operation == "add":
        toAdd = str(input("What would you like  to add? \n"))
        thelist.append(toAdd)
        marklist.append(False)
        pickle.dump(marklist, open("marklist.py", "r+b")) 
        pickle.dump(thelist, open("list.py", "r+b")) 
    if operation == "list":
        for q in range(len(thelist)):
            
            if marklist[q] == True:
                print(q+1,"[X]",thelist[q])
            else:
                print(q+1,"[ ]",thelist[q])
    if operation == "archive":
        for q in range(len(thelist)-1, -1, -1):

            if marklist[q] == True:
                del thelist[q]
                del marklist[q]
                pickle.dump(thelist, open("list.py", "r+b"))
                pickle.dump(marklist, open("marklist.py", "r+b"))

        for q in range(len(thelist)):
            if marklist[q] == True:
                print(q+1,"[X]",thelist[q])
            else:
                print(q+1,"[ ]",thelist[q])

    if operation == "mark":
        for q in range(len(thelist)):
            if marklist[q] == True:
                print(q+1,"[X]",thelist[q])
            else:
                print(q+1,"[ ]",thelist[q])
        toMark = int(input("Which one? \n"))
        if marklist[toMark-1] == False:
            marklist[toMark-1] = True
        else:
            marklist[toMark-1] = (False)
        pickle.dump(thelist, open("list.py", "r+b"))
        pickle.dump(marklist, open("marklist.py", "r+b")) 
        for q in range(len(thelist)):
            if marklist[q] == True:
                print(q+1,"[X]",thelist[q])
            else:
                print(q+1,"[ ]",thelist[q])

        
    else:
        thelist = pickle.load(open("list.py", "r+b"))
        marklist = pickle.load(open("marklist.py", "r+b"))
