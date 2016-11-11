import os
import time
import random


def table_init():
    """Initializes the tables."""

    new = []
    for i in range(0, 10):
        for j in range(0, 10):
            new.append(0)
        a_array.append(new)
        new = []
    for i in range(0, 10):
        for j in range(0, 10):
            new.append(0)
        b_array.append(new)
        new = []


def ai_shooting():
    """The AI takes a valid shoot to a random place."""

    global random_shooting
    while random_shooting == 1:
        x_coord = random.randint(0, 9)
        y_coord = random.randint(0, 9)
        if place_check(y_coord, x_coord, "none", 1, b_array):
            if ((b_array[y_coord][x_coord] == 3) or (b_array[y_coord][x_coord] == 4) or
                    (b_array[y_coord][x_coord] == 5) or (b_array[y_coord][x_coord] == 6)):
                b_array[y_coord][x_coord] = 1
                print_for_player(b_array)
                random_shooting = 0

            elif (b_array[y_coord][x_coord] == 0):
                b_array[y_coord][x_coord] = 2
                print_for_player(b_array)
                random_shooting = 0


def print_for_player(which_player, printtype="yours"):
    """Prints the talbe with nice format.
    If the printtype is "enemy", it prints only the hit or miss mark.
    If the printtype is on the default value, it prints the untouched ships too."""

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
                if which_player[i][o] == 0:
                    print("[ ]", end="")
                if which_player[i][o] == 1:
                    print("[X]", end="")
                if which_player[i][o] == 2:
                    print("[O]", end="")
                if which_player[i][o] == 3:
                    print("[S]", end="")
                if which_player[i][o] == 4:
                    print("[C]", end="")
                if which_player[i][o] == 5:
                    print("[M]", end="")
                if which_player[i][o] == 6:
                    print("[B]", end="")
                if o == 9:
                    print("\n")

            if printtype == "enemy":
                if which_player[i][o] in [0, 3, 4, 5, 6]:
                    print("[ ]", end="")
                if which_player[i][o] == 1:
                    print("[X]", end="")
                if which_player[i][o] == 2:
                    print("[O]", end="")
                if o == 9:
                    print("\n")


def text_to_int():
    """Converts a given char (A-J) to the corresponding number. (A = 0, J = 9)"""

    while True:
        input_char = input("Give the X coordinate! (A-J) ")
        if input_char == "exit":
            print("\nThe program will exit now. Bye!")
            exit()
        if input_char == "cheat":
            cheat()
            return input_char
        input_char = input_char.capitalize()
        for s in range(0, 10):
            if abc[s] == input_char:
                input_char = s
                return input_char
        else:
            print("\nNot correct char!\n")
            continue


def valid_int():
    """Checks the given number."""

    while True:
        inputint = input("Please add the Y coordinate! (1-10) ")
        if inputint == "exit":
            print("\nThe program will exit now. Bye!")
            exit()
        if inputint == "":
            print("\nYou did not added anything\n")
            continue
        try:
            inputint = int(inputint)
            if inputint in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                return inputint
            else:
                print("\nInvalid number!\n")
                continue
        except ValueError:
            print("\nThis is not a number!\n")
            continue


def orientation():
    """Checks the orientation key."""
    while True:
        input_orientation = input("Do you want it vertically? (Y/N) ")
        if input_orientation == "exit":
            print("\nThe program will exit now. Bye!")
            exit()
        if input_orientation in ["y", "Y", "n", "N"]:
            input_orientation = input_orientation.capitalize()
            return input_orientation
        else:
            print("\nWrong answer!\n")
            continue


def set_place(player):
    """Places the ships."""

    global a_array, b_array
    manual_set = input("Press enter to set the ships ")

    if manual_set == "test1":
        player = test_array1
        print("test_array1 maybe loaded")
    elif manual_set == "test2":
        player = test_array2
        print("test_array2 maybe loaded")

    else:
        print_for_player(player)
        ship_names = ["Submarine", "Cruiser", "Mothership", "Battleship"]
        for q in range(2, 6):  # A jatekos hajoi
            while True:
                print("Give the positions of the {}!  ".format(
                    ship_names[q - 2]))
                positionx = text_to_int()
                positiony = valid_int() - 1
                answer = orientation()
                if place_check(positiony, positionx, answer, q, player):
                    for index in range(q):
                        if answer == "N":
                            player[positiony][
                                index + positionx] = ships[q - 2][index]
                        if answer == "Y":
                            player[
                                index + positiony][positionx] = ships[q - 2][index]
                    break
                else:
                    print("\nInvalid position!!\n")
                    continue
            print_for_player(player)


def place_check(y, x, orientation, lenght, player):
    """Checks the places. If the place is out of the table, or contains ships, return False."""

    problem = 0
    if orientation == "none":  # SIMAshoot
        if (x > 9) or (y > 9) or (y < 0) or (x < 0) or (player[y][x] in [1, 2]):
            problem = 1

    if orientation == "Y":  # LEFELE
        for i in range(lenght):
            if (x > 9) or ((i + y) > 9) or (player[y + i][x] in [1, 2, 3, 4, 5, 6]):
                problem = 1

    if orientation == "N":  # OLDALRAFELE
        for i in range(lenght):
            if ((i + x) > 9) or (y > 9) or (player[y][x + i] in [1, 2, 3, 4, 5, 6]):
                problem = 1
    if problem == 1:
        return False
    else:
        return True


def shoot(player):
    """A players can take their shots. There is a feedback if the shot is a hit, a miss, or a ship shink."""

    array = []
    self_array = []
    global a_submarine, b_submarine, a_cruiser, b_cruiser, a_mothership, b_mothership, a_battleship, b_battleship
    global pa_submarine, pb_submarine, pa_cruiser, pb_cruiser, pa_mothership, pb_mothership, pa_battleship
    global pb_battleship, a_array, b_array
    submarine, cruiser, mothership, battleship, p_submarine, p_cruiser, p_mothership = 0, 0, 0, 0, 0, 0, 0
    p_battleship = 0
    if player == "Player 2":
        array = a_array
        self_array = b_array
        submarine, cruiser, mothership, battleship = a_submarine, a_cruiser, a_mothership, a_battleship
        p_submarine, p_cruiser, p_mothership, p_battleship = pa_submarine, pa_cruiser, pa_mothership, pa_battleship
    if player == "Player 1":
        array = b_array
        self_array = a_array
        submarine, cruiser, mothership, battleship = b_submarine, b_cruiser, b_mothership, b_battleship
        p_submarine, p_cruiser, p_mothership, p_battleship = pb_submarine, pb_cruiser, pb_mothership, pb_battleship
    print_for_player(self_array)
    print("      ↑↑↑↑↑↑↑ Your table ↑↑↑↑↑↑↑\n      ↓↓↓↓↓↓↓ Enemy table↓↓↓↓↓↓↓")
    print_for_player(array, "enemy")
    while True:
        print("This is your turn, ", player, ". take your shot! ")
        positionx = text_to_int()
        if positionx == "cheat":
            break
        positiony = valid_int() - 1
        if place_check(positiony, positionx, "none", 1, array):
            if array[positiony][positionx] == 0:
                array[positiony][positionx] = 2
                print_for_player(array, "enemy")
                print("MISS")

            if array[positiony][positionx] == 3:
                array[positiony][positionx] = 1
                print_for_player(array, "enemy")
                submarine -= 1
                if (submarine < p_submarine) and (submarine == 0):
                    print(player, "'s Submarine sank. ")
                p_submarine = submarine
                print("BÄMM")

            elif array[positiony][positionx] == 4:
                array[positiony][positionx] = 1
                print_for_player(array, "enemy")
                cruiser -= 1
                if (cruiser < p_cruiser) and (cruiser == 0):
                    print(player, "'s Cruiser sank. ")
                p_cruiser = cruiser
                print("BÄMM")

            elif array[positiony][positionx] == 5:
                array[positiony][positionx] = 1
                print_for_player(array, "enemy")
                mothership -= 1
                if (mothership < p_mothership) and (mothership == 0):
                    print(player, "'s Mothership sank. ")
                p_mothership = mothership
                print("BÄMM")

            elif array[positiony][positionx] == 6:
                array[positiony][positionx] = 1
                print_for_player(array, "enemy")
                battleship -= 1
                if (battleship < p_battleship) and (battleship == 0):
                    print(player, "'s Battleship sank. ")
                p_battleship = battleship
                print("BÄMM")

            if player == "Player 2":
                a_submarine, a_cruiser, a_mothership, a_battleship = submarine, cruiser, mothership, battleship
                pa_submarine, pa_cruiser, pa_mothership = p_submarine, p_cruiser, p_mothership
                pa_battleship = p_battleship
            if player == "Player 1":
                b_submarine, b_cruiser, b_mothership, b_battleship = submarine, cruiser, mothership, battleship
                pb_submarine, pb_cruiser, pb_mothership, pb_battleship = submarine, cruiser, mothership, battleship

            break
        else:
            ("Invalid location! Try again! ")
            continue


def player_switch():
    """Helps to stay the coords of the enemy ships secret."""

    input("Press enter if you done ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Switching players!")
    for i in range(5, 0, -1):
        print(i)
        time.sleep(1)
    print('\n' * 10)


def check_win():
    """This function finds out, who is the winner."""
    a, b = 0, 0
    for y in range(0, 9):
        for x in range(0, 9):
            if a_array[y][x] == 1:
                a += 1
    for y in range(0, 9):
        for x in range(0, 9):
            if b_array[y][x] == 1:
                b += 1

    if ((a_submarine == 0) and (a_battleship == 0) and (a_mothership == 0) and (a_cruiser == 0)) or (a > 13):
        print("\n\nPLAYER 2 WINS!!!" * 3)
        exit()
    if ((b_submarine == 0) and (b_battleship == 0) and (b_mothership == 0) and (b_cruiser == 0)) or (b > 13):
        print("\n\nPLAYER 1 WINS!!!" * 3)
        exit()


def player_versus_player():
    """Ship placing and battle until one of the player dies."""

    input("\nNow, you will place the ships. Player 1 starts first.\nPress enter to continue\n")
    table_init()
    set_place(a_array)
    player_switch()
    input("\nNow player 2 place their ships.\n")
    set_place(b_array)
    player_switch()
    while True:
        shoot("Player 1")
        check_win()
        player_switch()
        shoot("Player 2")
        check_win()
        player_switch()


def player_versus_enviroment():
    "Ship placing and battle versus the AI"
    print("Place your ships!")
    table_init()
    set_place(a_array)
    ai_ship_placement()
    while True:
        shoot("Player 1")
        input("Press enter ")
        check_win()
        artificial_intelligence()
        check_win()


def ai_ship_placement():
    """The ai places its ships."""

    for q in range(2, 6):
        while True:
            x_coord = random.randint(0, 9)
            y_coord = random.randint(0, 9)
            vertical_placement = random.randint(0, 1)
            if vertical_placement == 0:
                vertical_placement = "N"
            if vertical_placement == 1:
                vertical_placement = "Y"
            if place_check(y_coord, x_coord, vertical_placement, q, b_array):
                for index in range(q):
                    if vertical_placement == "N":
                        b_array[y_coord][index + x_coord] = ships[q - 2][index]
                    if vertical_placement == "Y":
                        b_array[index + y_coord][x_coord] = ships[q - 2][index]
            else:
                continue
            break


def artificial_intelligence():
    """The sequence about, the artificial intelligence performs shots."""

    while True:
        if ai_var == 2:
            bombardment()
            break
        if ai_var == 1:
            pos_checker()
            break
        if ai_var == 0:
            random_shooting()
            break


def random_shooting():
    """The AI takes a shoot to a random place."""
    global y_coord, x_coord, ai_var
    while True:
        x_coord = random.randint(0, 9)
        y_coord = random.randint(0, 9)
        if place_check(y_coord, x_coord, "none", 1, a_array):
            if ((a_array[y_coord][x_coord] == 3) or (a_array[y_coord][x_coord] == 4) or
                    (a_array[y_coord][x_coord] == 5) or (a_array[y_coord][x_coord] == 6)):
                a_array[y_coord][x_coord] = 1

                ai_var = 1

            elif (a_array[y_coord][x_coord] == 0):
                a_array[y_coord][x_coord] = 2

                ai_var = 0
            break
    # print_for_player(a_array)


def pos_checker():
    """If the random shot strikes, the AI is going to place shots around the previous location."""
    global y_coord, x_coord, ai_var, shoot_dir, y_pos_checker, x_pos_checker
    while True:
        if shoot_dir == 0:
            if place_check(y_coord - 1, x_coord, "none", 1, a_array):
                if a_array[y_coord - 1][x_coord] in [3, 4, 5, 6]:
                    a_array[y_coord - 1][x_coord] = 1
                    y_pos_checker, x_pos_checker = y_coord - 1, x_coord
                    ai_var = 2
                else:
                    a_array[y_coord - 1][x_coord] = 2
                    shoot_dir = 1
                break
            else:
                shoot_dir = 1
        if shoot_dir == 1:
            if place_check(y_coord, x_coord + 1, "none", 1, a_array):
                if a_array[y_coord][x_coord + 1] in [3, 4, 5, 6]:
                    a_array[y_coord][x_coord + 1] = 1
                    y_pos_checker, x_pos_checker = y_coord, x_coord + 1
                    ai_var = 2
                else:
                    a_array[y_coord][x_coord + 1] = 2
                    shoot_dir = 2
                break
            else:
                shoot_dir = 2
        if shoot_dir == 2:
            if place_check(y_coord + 1, x_coord, "none", 1, a_array):
                if a_array[y_coord + 1][x_coord] in [3, 4, 5, 6]:
                    a_array[y_coord + 1][x_coord] = 1
                    y_pos_checker, x_pos_checker = y_coord + 1, x_coord
                    ai_var = 2
                else:
                    a_array[y_coord + 1][x_coord] = 2
                    shoot_dir = 3
                break
            else:
                shoot_dir = 3
        if shoot_dir == 3:
            if place_check(y_coord, x_coord - 1, "none", 1, a_array):
                if a_array[y_coord][x_coord - 1] in [3, 4, 5, 6]:
                    a_array[y_coord][x_coord - 1] = 1
                    y_pos_checker, x_pos_checker = y_coord, x_coord - 1
                    ai_var = 2
                else:
                    a_array[y_coord][x_coord - 1] = 2
                    shoot_dir = 0
                    ai_var = 0
                break
            else:
                shoot_dir = 0
                ai_var = 0
                break
        break
    # print_for_player(a_array)


def bombardment():
    """If the pos_checker() finds the right direction, a bombardment session begins.
       After the spree ends, the AI will try a shot with the opposite direction."""

    global y_coord, x_coord, ai_var, shoot_dir, y_pos_checker, x_pos_checker
    if shoot_dir == 0:
        if place_check(y_pos_checker - 1, x_pos_checker, "none", 1, a_array):
            if a_array[y_pos_checker - 1][x_pos_checker] in [3, 4, 5, 6]:
                a_array[y_pos_checker - 1][x_pos_checker] = 1
                y_pos_checker, x_pos_checker = y_pos_checker - 1, x_pos_checker
            else:
                a_array[y_pos_checker - 1][x_pos_checker] = 2
                ai_var = 1
                shoot_dir = 2
        else:
            ai_var = 1
            shoot_dir = 2

    elif shoot_dir == 1:
        if place_check(y_pos_checker, x_pos_checker + 1, "none", 1, a_array):
            if a_array[y_pos_checker][x_pos_checker + 1] in [3, 4, 5, 6]:
                a_array[y_pos_checker][x_pos_checker + 1] = 1
                y_pos_checker, x_pos_checker = y_pos_checker, x_pos_checker + 1
            else:
                a_array[y_pos_checker][x_pos_checker + 1] = 2
                ai_var = 1
                shoot_dir = 3
        else:
            ai_var = 1
            shoot_dir = 3

    elif shoot_dir == 2:
        if place_check(y_pos_checker + 1, x_pos_checker, "none", 1, a_array):
            if a_array[y_pos_checker + 1][x_pos_checker] in [3, 4, 5, 6]:
                a_array[y_pos_checker + 1][x_pos_checker] = 1
                y_pos_checker, x_pos_checker = y_pos_checker + 1, x_pos_checker
            else:
                a_array[y_pos_checker + 1][x_pos_checker] = 2
                ai_var = 1
                shoot_dir = 0
        else:
            ai_var = 1
            shoot_dir = 0

    elif shoot_dir == 3:
        if place_check(y_pos_checker, x_pos_checker - 1, "none", 1, a_array):
            if a_array[y_pos_checker][x_pos_checker - 1] in [3, 4, 5, 6]:
                a_array[y_pos_checker][x_pos_checker - 1] = 1
                y_pos_checker, x_pos_checker = y_pos_checker, x_pos_checker - 1
            else:
                a_array[y_pos_checker][x_pos_checker - 1] = 2
                ai_var = 1
                shoot_dir = 1
        else:
            ai_var = 1
            shoot_dir = 1


def cheat():
    """Destroys all of the Player 2's, or AI's ship."""

    global b_submarine, b_battleship, b_mothership, b_cruiser
    b_submarine = 0
    b_battleship = 0
    b_mothership = 0
    b_cruiser = 0
    print("Player 2's ships destroyed ")


a_array = []
b_array = []

five_length_ship = [6, 6, 6, 6, 6]
four_length_ship = [5, 5, 5, 5]
three_length_ship = [4, 4, 4]
two_length_ship = [3, 3]

a_submarine, b_submarine = 2, 2
a_cruiser, b_cruiser = 3, 3
a_mothership, b_mothership = 4, 4
a_battleship, b_battleship = 5, 5

pa_submarine, pb_submarine = 2, 2
pa_cruiser, pb_cruiser = 3, 3
pa_mothership, pb_mothership = 4, 4
pa_battleship, pb_battleship = 5, 5


ships = [two_length_ship, three_length_ship,
         four_length_ship, five_length_ship]
ship_names = ["Submarine", "Cruiser", "Mothership", "Battleship"]
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

y_coord = 0
x_coord = 0
y_pos_checker = 0
x_pos_checker = 0
ai_var = 0
shoot_dir = 0

test_array1 = [[3, 4, 5, 6, 0, 0, 0, 0, 0, 0],
               [3, 4, 5, 6, 0, 0, 0, 0, 0, 0],
               [0, 4, 5, 6, 0, 0, 0, 0, 0, 0],
               [0, 0, 5, 6, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 6, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

test_array2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 6, 6, 6, 6, 6],
               [0, 0, 0, 0, 0, 0, 5, 5, 5, 5],
               [0, 0, 0, 0, 0, 0, 0, 4, 4, 4],
               [0, 0, 0, 0, 0, 0, 0, 0, 3, 3]]


def main():
    print("Welcome to our game!\n\nYou can choose between two game modes:\nPress P for PVP or ")
    print('Press E for PVE (play against A.I.)\n\nRemember, you can always quit, if you type "exit"\nHave fun :)')
    while True:
        gametype = input()
        if gametype in ["p", "P", "pvp", "PVP", "1"]:
            player_versus_player()
        elif gametype in ["e", "E", "pve", "PVE", "2"]:
            player_versus_enviroment()
        elif gametype == "exit":
            print("\nThe program will exit now. Bye!")
            exit()
        else:
            continue
try:
    main()
except Exception as error:
    print("Unfortunately, a problem occurred. The problem is:\n     ", error)
    print("We are sorry about that. The program will now exit.")
