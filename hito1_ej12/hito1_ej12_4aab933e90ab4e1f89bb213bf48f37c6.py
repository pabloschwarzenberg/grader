import random
x = (random.randint(1,20))
contador = 5
while contador >0:
    intento = eval(input("su numero:"))
    if intento ==x:
        print("Adivinaste, mi número era ",x)
        break
    if intento>x:
        print("mi número es menor")
        contador -=1
    else:
        print("mi número es mayor")
        contador -=1
else:
    print("No adivinaste, mi número era ",x)
    
