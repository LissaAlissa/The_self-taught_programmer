import re
line = 'Привидение прошуршало и исчезло в углу.'

m = re.findall('[аз]ло', line)

print(m)