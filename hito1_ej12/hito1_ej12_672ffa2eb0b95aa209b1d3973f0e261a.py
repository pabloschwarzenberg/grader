#Juego adivina mi número
import random
intentos = 0
numero = random.randint(1, 20)

while intentos < 6:
    print("adivina el numero: ")
    intento1 = input()
    intento1 = int(intento1)
    
    intentos = intentos + 1 
    
    if intento1 < numero:
      print("intenta otra vez: ")
    if intento1 > numero:
      print("intenta otra vez")    
    if intento1 == numero:
      break

if intento1 == numero:  
  intentos = str(intentos)
  print("adivinaste el numero era ",numero)
if intento1 != numero:
   numero = str(numero)
   print("no patetico, el numero era", numero)
    
  