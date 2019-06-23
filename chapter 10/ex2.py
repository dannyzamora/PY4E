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
    time = words[5]
    time = time.split(':')
    users[time[0]] = users.get(time[0],0)+1
print("DIC:", users)
lst = list(users.items())
# for k,v in users.items():
#     newtup = (k,v)
#     lst.append(newtup)
lst = sorted(lst)
print('LIST OF TUPLES:', lst)
for k,v in lst:
    print(k,v)
txt.close()
