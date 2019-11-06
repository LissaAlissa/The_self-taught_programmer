import random

def hangman(word):
    wrong = 0
    stages = ["",
                "___________            ",
                "|                      ",
                "|          |           ",
                "|          0           ",
                "|         /|\          ",
                "|         / \          ",
                "|                      "
    ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на казнь!") 

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '__' not in board:
            print("вы выиграли! Было загадано слово: ")
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print("Вы проиграли! Было загадано слово: {}.".format(word))

s = ["кот", "кит", "вор", "дом"]
s = random.choice(s)
hangman(s)

        