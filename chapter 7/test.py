try:
    txt = open('ex1.py')
except:
    print('File is not found')
    quit()
for line in txt:
    line = line.strip()
    print(line.upper())
txt.close()
