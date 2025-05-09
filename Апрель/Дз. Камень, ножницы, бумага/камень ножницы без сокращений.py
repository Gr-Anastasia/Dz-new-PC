import random

choise = {1 : "Камень", 2 : "Бумага", 3 : "Ножницы"}

def get_user_action():
    user_action = int(input("Выберите число:1 - Камень, 2 - Бумага или 3 - Ножницы: "))
    return choise[user_action]

def get_computer_action():
    possible_actions = ["Камень", "Бумага", "Ножницы"]
    computer_action = random.choice(possible_actions)
    return computer_action

def sravnenie(user_choise, comp_choise):
    if user_choise == comp_choise:
        print("Ничья!")
    elif user_choise == "Камень":
        if comp_choise == "Ножницы":
            print("Пользователь выбрал Камень. Вы выиграли!")
        else:
            print("Бумага накрывает камень. Вы проиграли!")
    elif user_choise == "Бумага":
        if comp_choise == "Камень":
            print("Пользователь выбрал Бумага. Вы выиграли!")
        else:
            print("Ножницы режут бумагу. Вы проиграли!")
    elif user_choise == "Ножницы":
        if comp_choise == "Бумага":
            print("Пользователь выбрал Ножницы. Вы выиграли!")
        else:
            print("Камень уничтожает ножницы. Вы проиграли!")

def isEnd():
    finish = input("Завершить игру? да или нет:  ")
    return finish == "да"
    
while True:
    user_choise = get_user_action()
    comp_choise = get_computer_action()
    print("Выбор компьютера: ", comp_choise)
    print("Выбор пользователя: ", user_choise)
    sravnenie(user_choise, comp_choise)
    if isEnd():
        break


