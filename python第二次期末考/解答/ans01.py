a = eval(input())
b = eval(input())
c = eval(input())

lst = [a,b,c]
lst.sort()

if lst[0]+lst[1] > lst[2]:
    print('True')
    if lst[0]**2 + lst[1]**2 == lst[2]**2:
        print('Right Triangle')
    else:
        print('Non-Right Triangle')

else:
    print('False')
