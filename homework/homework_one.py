import re
f = open("homework_files/a.txt")
for s in f:
    m = re.search(r'([а-я]{3,}[ое]\s[а-я]+(ть|ти|чь)|[а-я]+(ть|ти|чь)\s[а-я]{3,}[ое])([^а-я])', s)
    if m:
        print(m.group(1))