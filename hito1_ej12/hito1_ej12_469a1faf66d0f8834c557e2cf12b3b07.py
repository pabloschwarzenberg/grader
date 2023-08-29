#Juego adivina mi número
import random
comienza = random.randint(1, 20)
print(comienza)
intento = 5
num = 0
while (intento > 0 and comienza != num):
    num = int(input("Ingrese el numero que cree que es: "))
    if num > comienza:
        print("mi numero es menor")
        intento = intento - 1
        print(intento)
    elif (num < comienza):
        print("mi numero es mayor")
        intento = intento - 1
        print(intento)

if intento == 0:
    print("No adivinaste, mi numero era", comienza)
else:
    if comienza == num :
        print("Adivinaste, mi numero era", comienza)