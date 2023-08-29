#Juego adivina mi número
import random

numero_adiv= random.randint(1,20)
intentos=0

adivina=int(input("¿Cuál es mi numero en un rango del 1 al 20? : "))  

while intentos<5:
  if adivina>numero_adiv:
    adivina=int(input("Mi número es menor: "))    
  elif adivina<numero_adiv:
    adivina=int(input("Mi número es mayor: "))
  intentos=intentos+1      
if adivina==numero_adiv:
    print("Adivinaste, mi número era " + str(numero_adiv))
elif intentos==6:
    print("No adivinaste, mi número era " + str(numero_adiv))