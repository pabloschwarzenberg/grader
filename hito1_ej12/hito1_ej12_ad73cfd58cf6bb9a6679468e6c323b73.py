#Juego adivina mi número
import random

intentos = 0
min_numero = 1
max_numero = 20

print("Tienes 5 intentos para adivinar mi numero")


number = random.randint(min_numero, max_numero)
print("Estoy pensando en un numero entre" + str(min_numero)+ "-" + str(max_numero))

while intentos < 6:
numero = eval(input("Elige un numero: "))
    numero = int(numero)
    intentos = intentos + 1

    if numero < number:
        print("mi numero es mayor")
    if numero > number:
        print("mi numero es menor")
    if numero == number:
        break

if numero == number:
     
     number = str(number)
     print("Adivinaste, mi numero era", number) 
elif numero != number:
    number = str(number)
    print("No adivinaste, mi numero era", number)    