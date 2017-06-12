X=[]
while True:
    x = input()
    if x == '-1':
        break
    X.append(x)

max1 = 0

for i in X:
    if len(i)>max1:
        max1 = len(i)
        
for i in X:
    for j in range(max1-len(i)):
        print(' ',end='')
    print(i)
