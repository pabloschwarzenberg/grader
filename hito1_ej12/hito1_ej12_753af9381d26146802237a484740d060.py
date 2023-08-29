#Juego adivina mi número
import random
intentos = 0
NI = 1
NF = 20
numero = random.randint(str(NI),str(NF))
print("Adivina el número desde el 1 hasta el 20")
while(intentos < 6):
  print("intenta adivinar")
  se_estima = input()
  se_estima = int(se_estima)

  intentos = intentos + 1

  if(se_estim < numero):
    print("mi numero es mayor")
  if(se_estima > numero):
    print("mi numero es menor")
  if(se_estima == numero):
    break

if(se_estima == numero):
  intentos = str(intentos)
  print("Adivinaste, mi numero era ", numero) 
if(se_estima != numero):
  numero =str(numero)
  print("No adivinaste, mi numero era ", numero)