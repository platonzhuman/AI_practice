# !dmesg | head

# !seq 1 100000 > a.txt

# !seq 1 100000 2> b.txt

# !seq 1 100000 | tail | head -n 3

# !cat a.txt | grep -E "1{4}"

# import re # стандартная библиотека выражений
# f = open('a.txt')
# for s in f:
#   if re.search(r"21...", s): # функция которая принимает на вход патерн и строку где нужно найти этот патерн
#   #r - означает что все в одну строку что приходит
#     print(s, end="")

# import re # стандартная библиотека выражений
# f = open('a.txt')
# for s in f:
#   if re.search(r"^2\d*4$", s):
#     print(s, end="")

# import re # стандартная библиотека выражений
# f = open('a.txt')
# for s in f:
#   if re.search(r"^(2|3)\d*(4|5)$", s):
#     print(s, end="")

# import re # стандартная библиотека выражений
# f = open('a.txt')
# for s in f:
#   if re.search(r".*[02468]$", s):
#     print(s, end="")

# import re # стандартная библиотека выражений
# f = open('a.txt')
# for s in f:
#   if re.search(r"^..$", s):
#     print(s, end="")

# import re # стандартная библиотека выражений
# f = open('f2.txt.utf')
# for s in f:
#   if re.search(r"\d{2}\/\d{2}\/\d{4}", s):
#     print(s, end="")

# import re # стандартная библиотека выражений
# f = open('f2.txt.utf')
# for s in f:
#   if re.search(r"\((7|8)\)\d{10}\D", s):
#     print(s, end="")

# import re
# f = open("a.txt")
# for s in f:
#   pat = re.compile(r"1")
#   r = pat.sub(r'N', s)
#   print(r, end="")

# import re
# f = open("a.txt")
# for s in f:
#   pat = re.compile(r"[02468]$")
#   r = pat.sub(r'X', s)
#   print(r, end="")

# import re
# f = open("a.txt")
# for s in f:
#   pat = re.compile(r"1(\d)2")
#   r = pat.sub(r'x\1y', s)
#   print(r, end="")

# import re
# f = open("nobel_laur.txt")
# for s in f:
#   pat = re.compile(r"(.).+\s(.+)")
#   r = pat.sub(r'\2 \1.', s)
#   print(r, end="")

# import re
# f = open("f2.txt.utf")
# for s in f:
#   m = re.search(r"(\((7|8)\)\d{10})", s)
#   if m:
#     print(m.group(1))

# import re
# f = open("f2.txt.utf")
# for s in f:
#     m = re.search(r'([а-яё]{3,}[ое]\s[а-яё]+(ть|ти|чь)|[а-яё]+(ть|ти|чь)\s[а-яё]{3,}[ое])([^а-яё])', s)
#     if m:
#         print(m.group(1))

# import re
# f = open("f2.txt.utf")
# for s in f:
#     m = [x for x in re.split(r'([^аеёиоуыэюя]*[аеёиоуыэюя][^аеёиоуыэюя]*)', s) if x]
#     if m:
#         print(m)
