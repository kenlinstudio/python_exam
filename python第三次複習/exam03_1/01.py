x = int(input())

drinks = x
caps = x

while True:
    drinks = drinks + caps // 4
    caps = (caps%4) + (caps // 4)

    if caps == 3:
        drinks += 1
        break
    elif caps < 3:
        break

    
print(drinks)
