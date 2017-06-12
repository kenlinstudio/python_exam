

f1 = open('MathScoreFinal01.txt','r')
Final = f1.readlines()
f1.close()

f1 = open('MathScoreMid01.txt','r')
Mid = f1.readlines()
f1.close()

for i in range(len(Final)):
    Final[i] = Final[i].strip()
    Final[i] = Final[i].split(',')
 

for i in range(len(Mid)):
    Mid[i] = Mid[i].strip()
    Mid[i] = Mid[i].split(',')
 
Fail = []
Backward = 0
print('[Mean]')
for i in range(1,len(Final)):
    score = (eval(Mid[i][1])+eval(Final[i][1]))/2
    print('%s: %.2f'%(Mid[i][0],score))
    if score < 60:
        Fail.append(Mid[i][0])
    if eval(Final[i][1]) - eval(Mid[i][1]) < Backward:
        Backward = eval(Final[i][1]) - eval(Mid[i][1])



Fail2 = ' & '.join(Fail)
print('Fail: %s'%Fail2)

MaxBackWard = []
for i in range(1,len(Final)):
    if eval(Final[i][1]) - eval(Mid[i][1]) == Backward:
        MaxBackWard.append(Mid[i][0])
    
MaxBackWard2 = ' & '.join(MaxBackWard)
print('BackWard: %s'%MaxBackWard2)
