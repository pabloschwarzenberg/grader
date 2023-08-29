# completa el código de la función
import random
computador = random.randint(1,5)
while True:
  if(jugador < computador):
     i+=1
     print("Te he ganado,mi numero es",computador)
  elif (jugador==computador):
     print ("Empate")
  else:
     print ("Ganaste, mi numero es",computador)
  if(i == 3):
     break
     print ("Intentalo de nuevo")