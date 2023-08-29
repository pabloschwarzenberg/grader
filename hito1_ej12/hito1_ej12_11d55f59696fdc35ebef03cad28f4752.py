import random
scrt = random.randint(1, 20)
intentos = 5
while intentos > 0:
    z = eval(input())
    intentos -= 1
    if z > scrt:
        print("mi numero es menor")
    elif z < scrt:
        print("mi numero es mayor")
    else:
        print("Adivinaste, mi numero era"+ str(scrt))
        break
if intentos == 0:
    print("No adivinaste, mi numero era" + str(scrt))