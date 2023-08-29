#Juego adivina mi número
#Funciona en PyCharm pero tira un error EOF when reading a line
#ERROR ERROR	invalid syntax (hito1_ej12_8d9cc25d61b7cf05231438c3a36166d0.py, line 7)
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