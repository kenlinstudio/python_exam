s = eval(input())

def GPA(s):
    if 90<=s<=100:
        print(4.3)
        print('A+')
    elif 85<=s<=89:
        print(4.0)
        print('A')
    elif 80<=s<=84:
        print(3.7)
        print('A-')
    elif 77<=s<=79:
        print(3.3)
        print('B+')
    elif 73<=s<=76:
        print(3.0)
        print('B')
    elif 70<=s<=72:
        print(2.7)
        print('B-')
    elif 67<=s<=69:
        print(2.3)
        print('C+')
    elif 63<=s<=66:
        print(2.0)
        print('C')
    elif 60<=s<=62:
        print(1.7)
        print('C-')
    else:
        print(0)
        print('F')
       

GPA(s)
    
