import random

intentos = 0

print ("JUEGO DE AZAR....")

nombre = input("Cual es tu nombre?...")

x = random.randint (1, 20)

print ("Hola " + nombre + ", Bienvenido a mi primer juego...." )

while intentos < 6:
    intentos = intentos + 1
    numero = int(input("Elige un numero del 1 al 20"))
    
    if numero < x:
        print ("Tu numero es mas bajo")
    if numero > x:
        print ("Tu numero es mas alto")
    if numero == x:
        break

if numero == x:
    print ("Eres un genio....")
    print (nombre + " lo lograste con %d intentos" % (intentos))
    print ("Nos vemos....")
   
if numero != x:
    print ("Has perdido, sera en otra oportunidad...")
    print ("Nos vemos")