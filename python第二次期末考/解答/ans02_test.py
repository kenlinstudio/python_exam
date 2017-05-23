import time

tStart = time.time()
pro = 1
lst = []
while True:
    try:
        n = int(input())
        if n <= 0:
            n = int(input())
        else:
            for i in range(1,n+1):
                pro *=i
                lst.append(pro)
            print(sum(lst))
            break
    except:
        continue


tEnd = time.time()
print("It cost %f sec" %(tEnd - tStart))
