file = input('Enter the file name:')
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
    days[word] = days.get(word,0)+1
email = None
count = None
for k,v in days.items():
    if count is None or v > count:
        email = k
        count = v


print(email,count)
txt.close()
