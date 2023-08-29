#Juego adivina mi número
from random import randint
numero = randint(0,20)
numerojugador = 0
i = 1
while i < 6 and (numerojugador != numero):
  numerojugador = int(input("Ingrese su numero: "))
  i = i+1
  if numero > numerojugador:
      print("mi número es mayor")
  if numero < numerojugador:
      print("mi número es menor")
  if numerojugador == numero:
    print("Adivinaste, mi número era", numero)
    

if numerojugador != numero:
  print("No adivinaste, mi número era", numero)
