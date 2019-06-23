import re
txt = open('test.txt')
count = 0
lst = list()
for line in txt:
    line = line.rstrip()
    lst.extend(list(map(int,re.findall('New Revision: ([0-9]*)',line))))

print(sum(lst)/len(lst))
