max_sf = None
min_sf = None
#float("-inf")


while True:

    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        num = float(num)
        #    sum += num  math can be done here
        #    count += 1  and you won't beed the continue

    except:
        print('Invalid input')
        continue # this will start the next interation
    if max_sf is None or max_sf < num:
        max_sf=num
    if min_sf is None or min_sf > num:
        min_sf=num
print('Max: ', max_sf, ' Min: ',min_sf)
