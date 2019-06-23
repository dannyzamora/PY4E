file = 'test.txt'#input('Enter the file name:')
users = dict()
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
    users[word] = users.get(word,0)+1
lst = list()
for k,v in users.items():
    newtup = (v,k)
    lst.append(newtup)
lst = sorted(lst, reverse = True)

for k,v in lst[:1]:
    print(v,k)
txt.close()
