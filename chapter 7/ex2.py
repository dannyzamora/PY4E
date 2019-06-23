file = input('Enter the file name:')
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
    if line.startswith('X-DSPAM-Confidence:'):
        total += float(line[line.find(':')+1:])
        count += 1


print('Average spam confidence:',total/count)
txt.close()