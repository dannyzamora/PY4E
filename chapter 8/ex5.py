txt = open('test.txt')#input("Enter a file name: "))
count = 0
#l = 0  keeps tracks of each line
#word = list()
for line in txt:
    line = line.rstrip()
    #l += 1
    if not line.startswith("From "):
        continue
    line = line.split()
    #if line[1] not in word:
    #    word.append(line[1])

    print(line[1])
    #print(line[1], 'line :',l) same as above but shows which line from txt
    count += 1

print("There were",count, "lines in the file with From as the first word")
