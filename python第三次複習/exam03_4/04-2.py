X = []
while False==False:
    s = input()
    if s == '-1':
        break
    X.append(s)

max1 = 0
for i in X:
    if len(i) > max1:
        max1 = len(i)
        

for i in X:
    for j in range(max1-len(i)):
        print(' ',end="")
    print(i)
    
        
