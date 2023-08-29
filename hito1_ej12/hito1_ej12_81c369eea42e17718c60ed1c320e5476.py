#Juego adivina mi número
import random as rnd
n_secreto = rnd.randint(1, 20)
print(n_secreto)
intentos = 1
print("{0}° intento".format(intentos))
n = int(input("Adivina el numero secreto entre 1 y 20: "))


while (n != n_secreto) or (intentos < 5):
    if n < n_secreto:
        intentos += 1
        print("El numero secreto es mayor")
        print("{0}° intento".format(intentos))
        n = int(input("Adivina el numero secreto entre 1 y 20: "))
    elif n > n_secreto:
        intentos += 1
        print("El numero secreto es menor")
        print("{0}° intento".format(intentos))
        n = int(input("Adivina el numero secreto entre 1 y 20: "))
    if intentos == 5:
        break
    if n == n_secreto:
        print("¡Adivinaste!, el numero secreto era: {0}".format(n_secreto))
        break

if (n != n_secreto) and (intentos == 5):
    print("No adivinaste, el numero secreto era: {0}".format(n_secreto))
