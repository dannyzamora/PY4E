import re
txt = open('reg.txt')
count = 0
lst = list()
for line in txt:
    line = line.rstrip()
    lst.extend(list(map(int,re.findall('[0-9]+',line))))

print(sum(lst))
