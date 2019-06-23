try:
    score = input('Enter score: ')
    score = float(score)
    if score > 1.0 or score < 0.0:
        print('Bad score')
    else:
        if score >= .9:
            print('A')
        elif score >=.8:
            print('B')
        elif score >=.7:
            print ('C')
        elif score >=.6:
            print ('D')
        else:
            print('F')
except:
    print('Bad score')
