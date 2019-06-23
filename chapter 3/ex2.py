try:
    hours = input('Enter Hours: ')
    hours = float(hours)
    rate = input('Enter Rate: ')
    rate= float(rate)
    if hours > 40:
        pay = (hours-40)*rate*1.5
        pay = pay +40*rate
    else:
        pay = hours * rate

    print('Pay:', pay)
except:
    print('Error, please enter numericinput')
