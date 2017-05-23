n = eval(input())
 
 
sign = {'}':'{',']':'[',')':'(','>':'<'}
 
 
 
for i in range(n):
    try:
        context = input()
        l = []
        r = []
        for j in context:
            if j == '{'or j=='[' or j=='<' or j=='(':
                l.append(j)
 
            elif j == '}'or j==']'or j=='>' or j==')':
                if sign[j] == l[-1]:
                    l.reverse()
                    l.remove(sign[j])
                    l.reverse()
                else:
                    r.append()
            '''
            elif j == '}':
                if '{'in l :
                    l.remove('{')
                else:
                    r.append(j)
 
            elif j == ')':
                if '('in l :
                    l.remove('(')
                else:
                    r.append(j)
 
            elif j == ']':
                if '['in l :
                    l.remove('[')
                else:
                    r.append(j)
 
            elif j == '>':
                if '<'in l :
                    l.remove('<')
                else:
                    r.append(j)
             '''
        if len(l)==0 and len(r)==0:
            print('Y')
        else:
            print('N')
    except:
        print('N')
        continue
