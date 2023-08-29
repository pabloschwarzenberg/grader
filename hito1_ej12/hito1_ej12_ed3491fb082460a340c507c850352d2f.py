#Juego adivina mi número
import random
numero = random.randint(1,20)

print("Debes adivinar el numero en el que estoy pensando")
resultado = bool
intentos = 0
while intentos < 5:
    eleccion = int(input("Escoge un numero entre el 1 al 20"))
    if eleccion == numero:
       resultado = True
       break
    else:
       intentos = intentos + 1
       resultado = False
else:
    print("No adivinaste, mi número era %d" %(numero))
    
if resultado == True:
   print("Adivinaste, mi número era %d" %(numero))


       

  
