#Juego adivina mi número
import random
intentos=5
n=random.randint(1,20)
adivina=int(input("Adivina mi número!: "))
while adivina!=n:
    intentos=intentos-1
    if adivina==n:
        break
    if intentos==0:
        break
    if adivina>n:
        print("Mi número es menor al tuyo")
    if adivina<n:
        print("Mi número es mayor al tuyo")
    adivina=int(input("Intenta de nuevo, adivina mi número: "))
if intentos==0:
    print("No adivinaste, mi numero era ",n)
if adivina==n:
    print("Adivinaste, mi numero era",n)