#Juego adivina mi número
import random 
numero = int(random.randint(1,20))
contador = 0
print (numero)
while 1 == 1:
  if contador == 5:
    print ("No adivinaste, mi número era ",numero)
    break
  adivina = int(input("Adivina:"))
  if adivina == numero:
    print ("Adivinaste, mi número era ",numero)
    break
  if adivina != numero:
    contador = contador+ 1
    if adivina > numero:
      print("mi número es menor")
    if adivina < numero:
      print("mi número es mayor")