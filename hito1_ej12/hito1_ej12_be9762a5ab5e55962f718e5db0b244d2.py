#Juego adivina mi número
import random
num_intentos = 0
num_min = 1
num_max = 20
num_adivinar = random.randint(num_min,num_max)
print("Bienvenido a mi juego, estoy pensando un numero entre"+str(num_min)+ "y" +str(num_max))
while num_intentos<6:
    print("dime un numero: ")
    x1= input()
    x1= int(x1)
    num_intentos=num_intentos+1
    if x1 < num_adivinar:
        print("mi numero es mayor")
    if x1 > num_adivinar:
        print("mi numero es menor")
    if x1== num_adivinar:
        break
if x1==num_adivinar:
    print("adivinaste, mi numero era"+str(num_adivinar))
if x1!= num_adivinar:
    print("No adivinaste, mi número era"+str(num_adivinar))      