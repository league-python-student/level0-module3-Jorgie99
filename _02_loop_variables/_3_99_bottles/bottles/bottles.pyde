bottles = 99
str(bottles)
for i in range (99):
    if bottles > 0:
        print('' + str(bottles) + ' bottles of beer on the wall!')
        print('' + str(bottles) + ' bottles of beer!')
        print('Take one down, pass it around')
        bottles -= 1
        print('' + str(bottles) + ' bottles of beer on the wall!')
print('No bottles of beer on the wall! No bottles of beer! Go to the store and buy some more, 99 bottles of beer on the wall!')
