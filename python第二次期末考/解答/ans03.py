import math
n = eval(input())

score = math.sqrt(n)*10

print('Original: %.2f'%n)
print('Adjusted: %.2f(+%.0f)'%(score,(score-n)))
