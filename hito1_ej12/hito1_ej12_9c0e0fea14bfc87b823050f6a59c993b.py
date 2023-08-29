import random

intentos = 0



x = random.randint (1, 20)

while intentos < 5:
    intentos = intentos + 1
    c= int(input("Elige un numero del 1 al 20"))

    numero = int(c)
    if numero < x:
        print ("mi numero es menor")
    if numero > x:
        print ("mi numero es mayor")
    if numero == x:
        break

if numero == x:

    print ("Adivinaste, mi número era %d" % (x))

   
if numero != x:
    print ("No adivinaste, mi número era %d" % (x))

      