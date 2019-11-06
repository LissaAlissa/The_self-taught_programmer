people = {}
name = input('That your name? ')
names = {}
height = input('Enter your height: ')
names['height'] = height
weigh = input('Enter your weigh: ')
names['weigh'] = weigh
f_c = input('Enter your favorite_color: ')
names['favorite_color'] = f_c
f_a = input('Enter your favorite_actor: ')
names['favorite_actor'] = f_a
print(names)
people[name] = names

print(people)