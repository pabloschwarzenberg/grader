#Juego adivina mi número
import random
se = random.randint(1,20)
intentos = 0
 
while intentos <= 5:
    intentos = intentos + 1
    numero = int(input("Ingrese un numero :"))
    if numero == se:
      print("Adivinaste, mi número era ",se)
      break
    elif numero != se:
      if numero < se:
        print("el numero es mayor")
      else:
        print("el numero es menor")
    if intentos == 5:
     print("No adivinaste, mi número era ",se)
     break