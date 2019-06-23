def computegrade(s):
    if s >= .9:
        return 'A'
    elif s >=.8:
        return 'B'
    elif s >=.7:
        return 'C'
    elif s >=.6:
        return 'D'
    else:
        return 'F'
try:
    score = input('Enter score: ')
    score = float(score)
    if score > 1.0 or score < 0.0:
        print('Bad score')
    else:
        print(computegrade(score))



except:
    print('Bad score')
