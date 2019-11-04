import re

t = '__один__два__три__'

found = re.findall('__.*?__', t)

for match in found:
    print(match)