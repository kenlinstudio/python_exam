import time
 
a = eval(input())
st = time.localtime(a)
st2 = time.gmtime(a)
 
print(time.strftime('%Y-%m-%d %H:%M:%S', st2))
print(time.strftime('%Y-%m-%d %H:%M:%S', st))
