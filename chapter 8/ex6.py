nums = list()
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
    nums.append(num)
print('Max: ',max(nums), ' Min: ',min(nums))
