file = 'test.txt'#input('Enter the file name:')
days = dict()
try:
    txt = open(file)
except:
    print('File is not found')
    quit()
for line in txt:
    line = line.rstrip()
    words = line.split()
    if not line.startswith("From "):
        continue
    word = words[1]
    print(word)
    days[word] = days.get(word,0)+1

print(days)
txt.close()
