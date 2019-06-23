file = input('Enter the file name:')
try:
    txt = open(file)
except:
    print('File is not found')
    quit()
for line in txt:
    line = line.rstrip()
    print(line.upper())
txt.close()
