massive = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]


def func(massive):
    print("-----------")
    for i in range(3):
        for j in range(3):
            print("|" + massive[i][j] + "| ", end='')
        print()
        print("-----------")


def read_position():
    x = input("введите координату x" + " ")
    y = input("введите координату y" + " ")

    return x,y

def position_is_digit(x, y):
    if  not (x.isdigit() and y.isdigit()):
        print('не являются числами')
        return False
    return True

def is_correct_position(x, y):
    if not((0 <= x < 3) and (0 <= y < 3)):
        print('не входит в диапазон')
        return False

    if massive[x][y] != " ":
        print('zanyato')
        return False
    return True

def start_program():
    count = 0

    while True:
        if count == 9:
            print("ничья")
            break

        it_s_krestic = count % 2 == 0
        if it_s_krestic == True:
            print("сейчас ходит \"X\"")
        else:
            print("сейчас ходит \"O\"")
        x, y = read_position()

        if not position_is_digit(x, y):
            continue
        x = int(x)
        y = int(y)

        correct_position = is_correct_position(x, y)
        if correct_position == True:

            if it_s_krestic == True:
                massive[x][y] = "X"
            else:
                massive[x][y] = "O"

            if win_combination() == True:
                break
            count += 1

            func(massive)

        else:
            continue
def win_combination():
    check_win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 1), (1, 2)), ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)),
                 ((0, 2), (1, 2), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for massive_combination in check_win:
      symbols = []
      for cord in massive_combination:
        symbols.append(massive[cord[0]][cord[1]])
        if symbols == ["X", "X", "X"]:
            print(" выйграл  X")
            return True
        if symbols == ["O", "O", "O"]:
            print("выйграл O")
            return True

    return False
def greet():
    print("приветствуем в игре крестики- нолики")
    print("формат ввода X,Y")
    print("X - номер строки")
    print("Y - номер столбца")

greet()
start_program()
