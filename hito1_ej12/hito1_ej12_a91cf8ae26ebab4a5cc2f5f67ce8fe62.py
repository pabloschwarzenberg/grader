#Juego adivina mi número
import random
aleatorio = random.randint(1,20)
intentos = 0
while intentos <=5:
  #numero = int(input"ingrese un numero"))
  numero = 1
  if numero < aleatorio:
    print(" mi numero es mayor ")
    intentos += 1
  elif numero > aleatorio:
    print("mi numero es menor ")
    aleatorio += 1
  else:
        print("ganaste el numero era {}".format(aleatorio))
        break

if numero != aleatorio:
  print("perdiste, la respuesta correcta era {} ".format(aleatorio))  