#Juego adivina mi número
from random import randint
b=randint(1,20)
i=0
print(b)
while i<5:
    a = eval(input("Adivina el numero: "))
    if a==b:
        print("Adivinaste, mi número era",b)
        break
    if a>b:
        print("mi número es menor")
    else:
        print("mi número es mayor")
    i += 1
if i==5:
    print("No adivinaste, mi número era",b)