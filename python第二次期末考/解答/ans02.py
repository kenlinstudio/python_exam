while True:
    try:
        n = eval(input())
        if n <= 0:
            continue
        C = []
        for i in range(1,n+1):
            c = 1
            for j in range(1,i+1):
                c *= j
            C.append(c)
        break
    except:
        continue
print(sum(C))
