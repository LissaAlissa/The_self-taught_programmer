import re
l = "Красивое лучше, чем уродливое."
maches = re.findall("Красивое", l, re.IGNORECASE )

print(maches)