year = int(input('year = '))

if (year % 4 == 0 and year % 100 != 0) or year %  400 == 4:
    print('yes')
else:
    print('no')