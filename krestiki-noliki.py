# приветствие
def greeting():
    print("Сыграем в крестики-нолики?")
    agreement = input("Введи 'Да' или 'Нет'\n")
    if agreement.lower() == "да":
        print("Правила формата ввода данных в игре:")
        print("i j")
        print("где i - номер строки")
        print("где j - номер столбца\n")
    else:
        print("Хорошего дня. Пока!")
    return agreement.lower()


# игровое поле
field = [[" "] * 3 for i in range(3)]
def tictactoe_field():
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, str in enumerate(field):
        row = f"  {i} | {' | '.join(str)} | "
        print(row)
        print("  --------------- ")
    print()


# условие выигрыша
def check():
    winner = (((0, 0), (0, 1), (0, 2)),
              ((1, 0), (1, 1), (1, 2)),
              ((2, 0), (2, 1), (2, 2)),
              ((0, 0), (1, 0), (2, 0)),
              ((0, 1), (1, 1), (2, 1)),
              ((0, 2), (1, 2), (2, 2)),
              ((0, 2), (1, 1), (2, 0)),
              ((0, 0), (1, 1), (2, 2)))
    for coordinates in winner:
        matrix = []
        for c in coordinates:
            matrix.append(field[c[0]][c[1]])
            if matrix == ["X", "X", "X"]:
                print("Выигрывает X")
                return True
            if matrix == ["O", "O", "O"]:
                print("Выигрывает O")
                return True
    return False


# вопрос игрокам
def question():
    while True:
        coordinates = input("Введите 2 координаты: ").split()

        if len(coordinates) != 2:
            print("Необходимо ввести две коортинаты от 0 до 2")
            continue

        i, j = coordinates
        i, j = int(i), int(j)

        if 0 > i or i > 2 or 0 > j or j > 2:
            print("Координаты вне поля")
            continue

        if field[i][j] != ' ':
            print("Клетка занята, необходимо ввести другие координаты")
            continue

        return i, j


def game():
    game_over = False
    player1 = True
    k = 1
    while not game_over:
        tictactoe_field()
        k = k + 1
        if player1:
            print("Ходит X")
            i, j = question()
            field[i][j] = "X"
            player1 = False
        else:
            print("Ходит O")
            i, j = question()
            field[i][j] = "O"
            player1 = True
        if check():
            game_over = True
        elif k == 9:
            print("Ничья")
            break
        else:
            game_over = False


# запуск игры
start = 0
while True:
    if start == 0:
        if greeting() == 'да':
            game()
        else:
            break
    else:
        ask = input("Сыграем еще раз? Да/Нет\n")
        if ask.lower() == "да":
            field = [[" "] * 3 for i in range(3)]
            game()
        else:
            print("Хорошего дня. Пока!")
            break
    start = start + 1
