#Juego adivina mi número
#Juego adivina mi número
import random
intentos = 5
numerito = random.randint(1,20)

print("adivina mi numero entre 1 y 20")
print("introduce el numero que crees que es")
try:
    num_elegido = int(input())
except EOFError:
    print("no eof")

while intentos == 1:
    print("No adivinaste, mi número era",numerito)
    break
while num_elegido > numerito and intentos > 0:
    intentos = intentos - 1
    print("mi numero es menor")
    num_elegido = int(input())

while num_elegido < numerito and intentos > 0:
    intentos = intentos - 1
    print("mi numero es mayor")
    num_elegido = int(input())


while num_elegido == numerito:
    print("Adivinaste, mi número era",numerito)
    break      