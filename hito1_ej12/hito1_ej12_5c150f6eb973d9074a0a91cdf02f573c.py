#Juego adivina mi número
import random
intentosRealizados = 0

numero = random.randint(1,20)
num2 = int(input("ingresa el numero: "))
print('adivina el numero entre 1 y 20')

while intentosRealizados < 6:
    
     intentosRealizados = intentosRealizados + 1
     if num2 < numero:
        print("el numero es mayor")
     if num2 > numero:
          print("el numero es menor")
     if num2 == numero:
         break
if num2== numero:
     intentosRealizados = str(intentosRealizados)
     print("Adivinaste, mi número era ",numero)
if num2 != numero:
     numero = str(numero)
     print("No adivinaste, mi número era",numero)      