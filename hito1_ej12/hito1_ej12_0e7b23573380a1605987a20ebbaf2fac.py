#Juego adivina mi número
# mi número es menor o mi número es mayor
from random import randrange
x=(randrange(20))
Error=0

print(x)
print("Escoga un numero del 1 al 20")

while Error < 5:
    numero = int(input("Por favor ingrese el numero: "))
    if numero == x:
        print("Adivinaste, mi número era", x)
        break
    if numero > x:
        Error = Error + 1
        print("mi número es menor")
    elif numero < x:
        Error = Error + 1
        print("mi numero es mayor")
if Error == 5:
    print("No adivinaste, mi número era",x,)