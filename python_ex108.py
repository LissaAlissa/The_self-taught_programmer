try:
    a = input('enter number: ')
    b = input('enter 2 number: ')
    a = int(a)
    b = int(b)

    print(a/ b)
except (ZeroDivisionError, ValueError):
    print('Ошибка ввода')