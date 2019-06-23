hours = input('Enter Hours: ')
rate = input('Enter Rate: ')
if float(hours) > 40:
    pay = (float(hours)-40)*float(rate)*1.5
    pay = pay +float(40)*float(rate)
else:
    pay = float(hours)*float(rate)

print('Pay:', pay)
