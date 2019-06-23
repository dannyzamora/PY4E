def computepay(h,r):
    if h > 40:
        p = (h-40)*r*1.5
        p = p +40*r
    else:
        p = h * r

    return p


try:
    hours = input('Enter Hours: ')
    hours = float(hours)
    rate = input('Enter Rate: ')
    rate= float(rate)
    pay = computepay(hours,rate)
    print(pay)
except:
    print('Error, please enter numericinput')
