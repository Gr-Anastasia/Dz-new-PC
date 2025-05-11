import random

user_board = [["?", "?", "?"], ["?", "?", "?"], ["?", "?", "?"]]

def get_correct_board():
    correct_board = []
    for i in range(3):
        choice = ["@", "*", "@"]
        random.shuffle(choice)           
        correct_board.append(choice)
    return correct_board

def input_user():
    line = int(input("Введите строку (0, 1, 2):  "))
    column = int(input("Введите столбец (0, 1, 2):  "))
    return line, column

correct_board = get_correct_board()

def end_game(count):
    #count = 0
    #for k in user_board:
        #count += k.count("@")
    if count == 6:
        print("Вы победили!")
        #break
        return True

def game():
    count = 0
    print("Текущее поле: ") 
    for u in user_board:
        print(u)
    #print("Не забудь удалить в финале", correct_board)
    while True:
        line, column =  input_user()
        if correct_board[line][column] == "*":
            user_board[line][column] = "*"
            print("!БУМ!   Это мина!")
            print("Верное поле: ")
            for c in correct_board:
                print(c)
            break
        else:
            user_board[line][column] = "@"
            count += 1
            print("Попробуйте ещё раз")
            for u in user_board:
                print(u)
            if end_game(count):
                break
            
game()

