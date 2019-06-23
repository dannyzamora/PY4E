import re
reg = input('Enter a regular expression:')
txt = open('mbox.txt')
count = 0
for line in txt:
    line = line.rstrip()
    if re.search(reg,line):
        count += 1
print('mbox.txt had',count,'lines that matched')
