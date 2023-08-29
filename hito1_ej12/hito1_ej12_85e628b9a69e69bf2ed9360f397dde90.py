#Juego adivina mi número
import random

a=random.randint(1,20)
for i in range(5):
    b=int(input("Ingresa un número del 1 al 20: "))
    if a==b:
        print("Adivinaste, mi número era",a)
    elif a>b:
        print("Mayor")
    else:
        print("Menor")
print("No adivinaste, mi número era",a)