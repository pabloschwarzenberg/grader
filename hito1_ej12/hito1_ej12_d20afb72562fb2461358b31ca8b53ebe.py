#Juego adivina mi número
from random import *
nombre = input ("hola, ¿como te llamas?: ")
print(nombre, "adivina mi numero entre 1 y 20")
print("tienes 5 intentos")
intentos  = 0
numero = randint(1,20)
while intentos <= 5 :
    adivinar = int(input("ingresa un valor entre 1 y 20"))
    1<=adivinar<=20
    intentos = intentos + 1
    if adivinar < numero:
        print("tu numero ingresado es menor al numero secreto")
    elif adivinar > numero:
        print("tu numero ingresado es mayor al numero secreto")
    elif adivinar == numero:
        break
if numero == adivinar:
    print ("Adivinaste, mi numero era", numero)
elif numero != adivinar:
    print ("No adivinaste, mi numero era", numero)