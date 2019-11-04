a = input('Enter number: ')
b = input('Enter 2 number: ')
a = int(a)
b = int(b)
try:
    print(a / b)
except ZeroDivisionError:
    print('b не может быть нулевым.')