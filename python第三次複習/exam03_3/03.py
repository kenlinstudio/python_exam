a1 = int(input())
r = eval(input())
n = int(input())

X = [a1]

for i in range(n-1):
    a1 = a1*r
    X.append(a1)
print(X)
print(sum(X))

#注意一下如何控制這個輸出格式：
print('注意一下如何控制這個輸出格式，如下：')
for i in range(len(X)):
    if i != len(X)-1:
        if X[i] < 0:
            print('(%d)'%X[i],'+ ',end="")
        else:
            print(X[i],'+ ',end="")
    else:
        if X[i] < 0:
            print('(%d)'%X[i],'= ',end="")
        else:
            print(X[i],'= ',end="")
print(sum(X))
