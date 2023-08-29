#Juego adivina mi número
import random
num = random.randint(1,20)
n = 1
while n<=5:
    intento = int(input("Adivina número: "))
    if intento<num:
        print("Mi número es mayor")
    elif intento>num:
        print("Mi número es menor")
    else:
        print("Adivinaste, mi número era",num )
        break
    if n == 5:
        print("No adivinaste, mi número era",num )
    n += 1      