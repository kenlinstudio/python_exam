X = []
while True:
    x = eval(input())
    if x == -1:
        break

    X.append(x)

summation = 0
for i in X:
    if i > 30:
        summation += i
      
Y = X.copy()
Y.sort()

print(X)
print(Y)
print(summation)
