f1 = open('../app/score.csv','r')
data = f1.readlines()
f1.close()

MathPass=[]
EngPass = []
MathPassEngFail = []

for i in range(len(data)):
    data[i]= data[i].strip()
    data[i]=data[i].split(',')
for i in range(1,len(data)):
    if int(data[i][1])>= 60:
        MathPass.append(data[i][0])
    if int(data[i][2])>= 60:
        EngPass.append(data[i][0])
    if int(data[i][2]) < 60 and int(data[i][1])>= 60:
        MathPassEngFail.append(data[i][0])
Total = len(data)-1

MathPass.sort()
EngPass.sort()
MathPassEngFail.sort()

print(MathPass)
print(EngPass)
print(MathPassEngFail)
print(Total)
