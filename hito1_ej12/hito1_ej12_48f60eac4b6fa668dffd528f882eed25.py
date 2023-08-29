#Juego adivina mi número
from random import randint
print("Adivine el numero secreto")
randomValue = randint(1, 20)
valorUsuario = 0
intentos = 0 
while (valorUsuario != randomValue):
    if (intentos == 5):
        break
    valorUsuario = int(input("ingrese el numero secreto\n"))
    if (valorUsuario > randomValue):
        print("El numero secreto es menor a " + str(valorUsuario))
    if (valorUsuario < randomValue):
        print("El numero secreto es mayor a " + str(valorUsuario))
    intentos = intentos + 1
    print("lleva  " + str(intentos) + "  intentos" )
    if (valorUsuario > 10):
        print ("error, su numero es mas grande que el asignado, vuelva a intentarlo")
    if (valorUsuario < 0):
        print ("error, su numero es mas pequeño que el asignado, vuelva a intentarlo")
if (valorUsuario == randomValue):   
    print ("Adivinaste, mi número era" + str(randomValue))
if (intentos == 5):
    print("No adivinaste, mi número era" + str(randomValue))