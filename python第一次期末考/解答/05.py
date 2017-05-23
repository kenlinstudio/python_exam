f1 = open('../app/math_list.csv','r',encoding='big5')
math_list = f1.readlines()
f1.close()

f2 = open('../app/english_list.csv','r',encoding='big5')
eng_list = f2.readlines()
f2.close()

for i in range(len(math_list)):
    math_list[i] = math_list[i].strip()
    math_list[i] = math_list[i].split(',')
    
for i in range(len(eng_list)):
    eng_list[i] = eng_list[i].strip()
    eng_list[i] = eng_list[i].split(',')
    
math_set = set()
for i in range(len(math_list)):
    if i ==0:
        continue
    math_set.add(math_list[i][0])
    
eng_set = set()
for i in range(len(eng_list)):
    if i ==0:
        continue
    eng_set.add(eng_list[i][0])

all_set = math_set.union(eng_set)
    
ans1 = list(math_set.intersection(eng_set))
ans1.sort()

ans2 = list(all_set-math_set.intersection(eng_set))
ans2.sort()

ans3 = list(math_set.difference(eng_set))
ans3.sort()

ans4 = list(eng_set.difference(math_set))
ans4.sort()

ans5 = list(all_set)
ans5.sort()

print(ans1)
print(ans2)
print(ans3)
print(ans4)
print(ans5)
