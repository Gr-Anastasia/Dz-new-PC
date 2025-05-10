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
    column = int(input("Введите столбец (0, 1, 2):  "))
    line = int(input("Введите строку (0, 1, 2):  "))
    return column, line

correct_board = get_correct_board()


def game():
    print("Поле", user_board)
    column, line =  input_user()
    if correct_board[column][line] == "*":
        user_board[column][line] = "*"
        print("Это мина")
        print(user_board)
        
    else:
        user_board[column][line] = "@"
        print("Попробуйте ещё раз")
        
    
game()

    



