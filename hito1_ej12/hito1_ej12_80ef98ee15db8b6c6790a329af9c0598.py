#Juego adivina mi número
import time
import sys
import random

N = random.randint(1, 20)

C = 0

print("Bienvenido al juego de adivina mi numero, tienes 5 intentos para adivinar un numero del 1 al 20 , ingrese su primer intento")

X = int(input())

while C < 5:
    if X < 0 or X > 20:      
        print("PORFAVOR ingresar un numero del 1 al 20")
    elif X == N:
       print("Ganaste en el primer intento! el numero era:")
       print (N)
       time.sleep(999)
       C = C=+ 10
    elif X < N:
        print("Es un numero mas alto, siga intentando")
        C =+ 1
    elif X > N:
        print("Es un numero mas bajo, siga intentando")
        C =+ 1
    break

print("2do intento")
X = int(input())

while C < 5:
    if X < 0 or X > 20:
        
        print("PORFAVOR ingresar un numero del 1 al 20")
    elif X == N:
         print("Ganaste en el segundo intento, felicidades,el numero era:")
         print (N)
         C = C=+ 10
         time.sleep(999)
    elif X < N:
        print("Es un numero mas alto, siga intentando")
        C =+ 1
    elif X > N:
        print("Es un numero mas bajo, siga intentando")
        C =+ 1
    break
print("3cer intento")
X = int(input())
while C < 5:
    if X < 0 or X > 20:
        
        print("PORFAVOR ingresar un numero del 1 al 20")
    elif X == N:
        print("Ganaste en el tercer intento, felicidades! el numero era:")
        print(N)
        C = C=+ 10
        time.sleep(999)
    elif X < N:
        print("Es un numero mas alto, siga intentando")
        C =+ 1
    elif X > N:
        print("Es un numero mas bajo, siga intentando")
        C =+ 1
    break

print("4to intento")
X = int(input())
while C < 5:
    if X < 0 or X > 20:
        
        print("PORFAVOR ingresar un numero del 1 al 20")
    elif X == N:
        print("Ganaste en el 4to intento, felicidades!, El numero era")
        print(N)
        C = C=+ 10
        time.sleep(999)
        
    elif X < N:
        print("Es un numero mas alto, siga intentando")
        C =+ 1
    elif X > N:
        print("Es un numero mas bajo, siga intentando")
        C =+ 1
    break

print("5to intento")
X = int(input())
while C < 5:
    if X < 0 or X > 20:
        
        print("PORFAVOR ingresar un numero del 1 al 20, intentelo de nuevo")
    elif X == N:
       print("Ganaste en el ultimo intento, felicidades!, el numero era:")
       print(N)
    
    elif X < N:
        print("Lamentablemente has perdido :(, el numero era:")
        print(N)
        C =+ 1
    elif X > N:
        print("Lamentablemente has perdido :(, el numero era: ")
        print(N)
        C =+ 1
    break