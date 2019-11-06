i = input('How old are you? ')

with open('old.txt', 'w') as f:
    f.write(i)