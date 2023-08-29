#Juego adivina mi número
import numpy as np
print("Adivina mi número - Tienes 5 intentos")
numero = np.random.randint(1,20)
resultado = 0
intentos = 1
while (resultado ==0) and (intentos <=5):
  adiv = int(input("Cual crees que es: "))
  if (numero > adiv):
    print("Mi numero es mayor")
  elif (numero < adiv):
    print("Mi numero es menor")
  else: 
    resultado = 1
  if (intentos == 5):
    resultados = -1
  intentos +=1

if (resultado == 1 ):
  print("Adivinaste, mi numero era el ",numero)
  print("No fue tan dificil, verdad")
else:
  print("NO adivinaste, mi numero era el ",numero)
  print("Suerte la proxima vez")