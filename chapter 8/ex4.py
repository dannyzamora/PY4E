file =  't.txt' #input('Enter file:')
txt = open(file)
words = list()
for line in txt:
    line = line.rstrip()
    wds = line.split()
    #wds = list(set(wds))

    #w1 = [w for w in wds if w not in words]
    #
    #words.extend(w1)
    #print(words)
    #words.extend([w for w in wds if w not in words])


    #print(words)
    #words = list(set(words)|set(wds))

    for w in wds:           # PY4E only
        if w not in words:  #  accepted
            words.append(w) # this code

#words.sort()
print(sorted(words))
