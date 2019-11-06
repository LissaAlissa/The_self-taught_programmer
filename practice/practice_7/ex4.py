print("Для выхода нажмите Х.")
nums = [2, 4, 6, 9, 3]

while True:
    for x in nums:
        y = input("Введите число: ")
        if y == "Х":
            break
        
        y = int(y)
        if y == x:
            print("Вы угадали!!!")
        else:
            print("Попробуйте еще раз!")
