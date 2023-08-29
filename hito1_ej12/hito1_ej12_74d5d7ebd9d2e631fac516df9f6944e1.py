#Juego adivina mi número
import random



print("hola")
numero = random.randint(1, 20)

print(" pienso entre el 1 y 20.")

while intentosRealizados < 6: print("adivina.")
estimacion = input()

estimacion = int(estimacion)



intentosRealizados = intentosRealizados + 1


if estimacion < numero: print("Tu estimación es muy baja.") 


if estimacion > numero: print("Tu estimación es muy alta.")

if estimacion == numero:
 break
if estimacion == numero:

     intentosRealizados = str(intentosRealizados)
print("Adivinaste, mi numero era " + intentosRealizados + "intentos")
if estimacion != numero: numero= str(numero)
print("no adivinaste, mi numero era " + numero) 


