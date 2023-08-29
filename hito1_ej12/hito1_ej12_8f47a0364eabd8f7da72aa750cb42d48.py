import random
intentos = 0
print ("JUEGO DE AZAR....")
nombre=str(input("Ingresa tu nombre: "))
x=random.randint (1, 20)
print("Hola!", nombre, "bienvenido/a")
while intentos <= 5:
    intentos = intentos + 1
    print ("Elige un numero del 1 al 20")
    numero=int(input("Ingresa un numero: "))
    if numero<x:
        print ("Mi número es mayor")
    if numero>x:
        print ("Mi número es menor")
    if numero==x:
        print("Adivinaste, mi número era: ",x)
        break
if intentos ==0 and numero!=x:
    print("No adivinaste, mi numero era: ",x)