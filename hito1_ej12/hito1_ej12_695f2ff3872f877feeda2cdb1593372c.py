#Juego adivina mi número
import random
i=0
while i<5:
    jugador=int(input("Ingrese un numero entre 1 y 20:"))
    computador=random.randint(1,20)
    if (jugador < computador):
        print("el numero ingresado es menor")
    else:
        print("el numero ingresado es mayor")
    if (jugador == computador):
      print("Adivinaste, mi número era:",computador)
    else:
      i=i+1
if (i>4):
  print("No adivinaste, mi número era:",computador)

