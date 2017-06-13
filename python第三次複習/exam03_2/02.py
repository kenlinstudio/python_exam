X = []
while 1 == 1:
    a = input()
    try:
        a = eval(a)
    except:
        print("請輸入數字")
        continue

    if a == -1:
        break
    X.append(a)

    
Y = X.copy()

print(X)
X.sort()

print(X)
print(Y)
