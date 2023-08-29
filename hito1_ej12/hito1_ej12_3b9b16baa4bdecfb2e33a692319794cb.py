#Juego adivina mi número
from random import:
intentos=5
numero = randint (1,20)
while intentos > 0:
    estimacion=int(input())
    if estimacion < numero:
      print("mi numero es mayor")
    elif estimacion > numero :
      print("mi numero es menor")
    elif estimacion==numero:
          break
if numero == estimacion:
    print("Adivinaste, mi numero era", (numero))
elif numero != estimacion: 
    print("No adivinaste, mi numero era", (numero))