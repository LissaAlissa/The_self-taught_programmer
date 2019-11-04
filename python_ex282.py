import re

line = "Я тебя $"
m = re.findall('\\$', line, re.IGNORECASE)

print(m)