colors = [
    "фиолетовый",
    "ораньжевый",
    "зеленый"
]
guess = input('Угадайте цвет: ')

if guess in colors:
    print('Вы угадали!')
else:
    print('Неправильно! Попробуйте еще.')