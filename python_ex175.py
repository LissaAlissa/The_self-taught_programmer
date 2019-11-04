equ = 'Все животные одинаковы.'
#equ = equ.replace("о", "@")
print(equ)

f = equ.replace('одинаковы', "посвоему {}".format('хороши'))
print(f)