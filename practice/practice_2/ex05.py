
s = input('Enter number: ')

try:
    def f():   
        ''' Переобразовывает строку в float'''
        return float(s)
    print(f())
except ValueError:
    print('Input error!')

