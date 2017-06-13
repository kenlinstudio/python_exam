f1 = open('MathScoreFinal01.txt','r')
Final = f1.readlines()
f1.close()

f1 = open('MathScoreMid01.txt','r')
Mid = f1.readlines()
f1.close()

for i in range(len(Mid)):
    Mid[i] = Mid[i].strip().split(',')
for i in range(len(Final)):
    Final[i] = Final[i].strip().split(',')


print('[Mean]')

Num = []
max1 = 1000
for i in range(1,len(Mid)):
    mean = (eval(Mid[i][1]) + eval(Final[i][1]))/2
    diff = eval(Final[i][1]) - eval(Mid[i][1])
    if diff < max1:
        max1 = diff
    if mean < 60 :
        Num.append(Mid[i][0])
    print('%s: %.1f'%(Mid[i][0],mean))
Num2 = " & ".join(Num)
print('Fail:',Num2)

Fail2 = []
for i in range(1,len(Mid)):
    if eval(Final[i][1]) - eval(Mid[i][1]) == max1:
        Fail2.append(Mid[i][0])

Fail2 = " & ".join(Fail2)
print('BackWard:',Fail2)
