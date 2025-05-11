import random

user_board = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]

def get_correct_board():
    correct_board = []
    for i in range(3):
        cell = []
        for j in range(3):
            possible_actions = ["@", "*"]
            computer_board = random.choice(possible_actions)
            cell.append(computer_board)
        correct_board.append(cell)
    return correct_board

def input_user():
    line = int(input("Введите строку (0, 1, 2):  "))
    column = int(input("Введите столбец (0, 1, 2):  "))
    return line, column

correct_board = get_correct_board()

def game():
    print("Текущее поле: ")
    for u in user_board:
        print(u)
    print("Не забудь удалить в финале", correct_board)
    while True:
        line, column =  input_user()
        if correct_board[line][column] == "*":
            user_board[line][column] = "*"
            print("!ВЗРЫВ!   Это мина!")
            print("Верное поле: ")
            for c in correct_board:
                print(c)
            break
        else:
            user_board[line][column] = "@"
            print("Попробуйте ещё раз")
            for u in user_board:
                print(u)
                   
game()
