def place_checke(x, y, orientation, lenght, player):
    """Checks the places. If the place is out of the table, or contains ships, return False."""
    problem = 0
    if orientation == "Y":      #LEFELE
        for i in range(lenght):
            if (x>9) or (y>9) or (player[x][y] in [3, 4, 5, 6]):
                problem = 1
            y += 1
                
    if orientation == "N":      #OLDALRAFELE
        for i in range(lenght):
            if (x>9) or (y>9) or (player[x][y] in [3, 4, 5, 6]):
                problem = 1
            x += 1
    if problem == 1:
        return False
    else:
        return True
fivelengthship = [6, 6, 6, 6, 6]
fourlengthship = [5, 5, 5, 5]
threelengthship = [4, 4, 4]
twolengthship = [3, 3]
aArray = []
bArray = []

new = []
for i in range(0, 10):  # tömbök inicializálása
    for j in range(0, 10):
        new.append(0)
    aArray.append(new)
    new = []
for i in range(0, 10):
    for j in range(0, 10):
        new.append(0)
    bArray.append(new)
    new = []

print(place_check(1, 1, "N", 5, aArray))