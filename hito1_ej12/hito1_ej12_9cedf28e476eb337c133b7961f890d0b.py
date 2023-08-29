#Juego adivina mi número
import random

minimo = 1
maximo = 20
totalintentos = 0
numero = random.randint(minimo, maximo)
while totalintentos < 5:
   intento = int(input("Escoge un numero: "))
   totalintentos = totalintentos + 1
   if intento < numero:
      print("mi numero es menor")
   if intento > numero:
      print("mi numero es mayor")
   if intento == numero:
      break
if intento == numero:
   totalintentos = str(totalintentos)
   print("Adivinaste, mi numero era {}".format(numero))
if intento != numero:
   print("No adivinaste, mi numero era {}".format(numero))      