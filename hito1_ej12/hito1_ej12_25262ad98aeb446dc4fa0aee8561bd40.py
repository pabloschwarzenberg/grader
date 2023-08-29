#Juego adivina mi número
from random import randint
 
num = randint(1,20)
intentos = 0

def finJuego():
  if intentos == 4:
    return True
  else:
    return False


while True:
  user_in = int(input("Ingresa un numero: "))
  if user_in == num:
    print("Adivinaste, mi numero era " + str(num))
    break
  else:
    if (user_in>num) and (finJuego() == False):
      print("mi numero es menor")
      intentos += 1
    elif (user_in<num) and (finJuego() == False):
      print("mi numero es mayor")
      intentos += 1
    else:
      print("No adivinaste, mi numero era " + str(num))
      break