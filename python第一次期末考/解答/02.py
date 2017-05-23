t = input()
# 111,222,333,444,555,666,789,987,876,678,765,567
# 2017,1231,1993,512,2897,3901,2004,1143,2200,524
# 1,3,5,7,9,11,13,15,17,21,33,35,37,2
# 200,400,800,600,333,222,111,222,54,2332,4413
lis=t.split(',')

odd = 0
even = 0
summation = 0
for i in lis:
    if int(i)%2 == 1:
        odd += int(i)
    if int(i)%2 == 0:
        even += int(i)
    summation += int(i)

print(odd)
print(even)
print(summation)
