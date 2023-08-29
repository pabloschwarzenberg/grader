import random

intentos = 0


x = random.randint (1, 20)


while intentos < 5:
     intentos = intentos + 1
     numero=input("Elige un numero del 1 al 20")


     numero = int(numero)
     if numero < x:
        print ("Mi numero es mayor")
     if numero > x:
        print ("Mi numero es menor")
     if numero == x:
         print("Adivinaste, mi numero era {}".format(x))
         break
     elif intentos > 6:
         print("No adivinaste, mi número era {}".format(x) )