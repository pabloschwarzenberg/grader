#Juego adivina mi número
import random
numeroSecreto = random.randint(1,20)
print(numeroSecreto)
numero = int(input('Adivine el número secreto¡¡.Ingrese un número:'))
contador=0
while(numeroSecreto != numero):
 
    contador=contador+1
    if numero >numeroSecreto:
        print("mi número es menor")
        numero = int(input('Adivine el número secreto¡¡.Ingrese un número:'))
    if numero <numeroSecreto:
        print("mi número es mayor")
        numero = int(input('Adivine el número secreto¡¡.Ingrese un número:'))
    if contador==5:
        print("no acertaste porfavor intenta nuevamente mi numero era",numeroSecreto)
        break

if numero==numeroSecreto:

  print("Adivinaste,mi numero era:",numeroSecreto)