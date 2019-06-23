file = input('Enter the file name:')
if 'na na boo boo' in file.lower():
    print("OH NO! HERE WE GO AGAIN")
    quit()
try:
    txt = open(file)
except:
    print('File is not found')
    quit()
total = 0.0
count =0
curr = 0.0
for line in txt:
    line = line.rstrip()
    if line.startswith('X-DSAM-Confidence:'):
        total += float(line[line.find(':')+1:])
        count += 1

    print(total,count)
print('Average span confidence:',total/count)
txt.close()
