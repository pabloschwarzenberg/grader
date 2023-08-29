#Juego adivina mi número
from random import randint
numero_adivinar = randint(1,20)
intentos = 0
while (intentos<5):
    numero = int(input("Ingrese numero entre 1 a 20: "))
    intentos = intentos + 1
    if numero == numero_adivinar:
        print ("Adivinaste, mi número era",numero_adivinar)
        intentos = 6
    elif numero > numero_adivinar:
        print ("Mi número es menor")
    elif numero < numero_adivinar:
        print ("Mi número es mayor")
print ("No adivinaste, mi numero era", numero_adivinar)