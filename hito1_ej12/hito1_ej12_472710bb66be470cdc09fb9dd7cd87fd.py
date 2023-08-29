#Juego adivina mi número
import  random

indicar_numero = random.randint(1,20)

S = 1

while S<=5 :
   ADIVINA = int(input("adivina el numero: "))
   if ADIVINA<indicar_numero:
      print("Mi numero es mayor")
   elif ADIVINA>indicar_numero:
      print("Mi numero es menor")
   else :
      print("Adivinaste, mi número era " ,indicar_numero)
      break
   if S==5 :
      print("No adivinaste, mi número era " , indicar_numero)
   S += 1