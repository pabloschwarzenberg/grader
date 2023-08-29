#Juego adivina mi número
import random
aleatorio = random.randint(1,20)
intentos = 0
while intentos <=5:
#numero = int(input"ingrese un numero")) Profesor, active esta linea y borre la de abajo
numero = 1
if numero < aleatorio:
    print(" Mi numero es mayor ")
    intentos += 1
elif numero > aleatorio:
    print("Mi numero es menor ")
    aleatorio += 1
else:
        print("Ganaste el numero era {}".format(aleatorio))
        break

if numero != aleatorio:
  print("Perdiste, la respuesta correcta era {} ".format(aleatorio))        