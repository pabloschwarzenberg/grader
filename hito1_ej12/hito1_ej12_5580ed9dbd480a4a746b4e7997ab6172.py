#Juego adivina mi número
import random
intentos= 0
n = random.randint(1, 20)
print("Intenta adivinar.")
estimado= int(input("Ingrese su numero estimado: "))


while intentos < 5:

    if estimado < str(n):
        print("Tu estimación es  menor al numero")
        intentos = intentos + 1
    if estimado > n:
        print("Tu estimación es mayor al numero")
        intentos= intentos+ 1
    if estimado == n:
        break
    estimado= (input("Ingrese su numero estimado: "))

if estimado == n:
    intentos = (intentos)
    print("Buen trabajo, adivinaste el numero")

if estimado != n:
    n = str(n)
    print("No adivinaste, mi numero era:" + n)