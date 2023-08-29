#Juego adivina mi número
import random
intentos_realizados = 0

numero = random.randint(1,20)
while intentos_realizados< 5:
   print("intenta adivinar")
   estimacion=input()
   estimacion=int(estimacion)

   intentos_realizados=intentos_realizados + 1

   if estimacion < numero:
     print("Mi numero es mayor")

   if estimacion > numero:
     print("Mi numero es menor")

   if estimacion == numero:
     print("Adivinaste, mi numero era"+"  "+numero)

if estimacion != numero:
   numero = str(numero)
   print("No adivinaste, mi numero era"+"  "+numero)