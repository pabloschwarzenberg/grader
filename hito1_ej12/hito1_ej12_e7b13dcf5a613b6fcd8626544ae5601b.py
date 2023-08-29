#Juego adivina mi número
import random
num1 = random.randint(1,20)

for i in range(1,6):
    print("Intento n° %i"%(i))
    num2 = int(input("Ingrese número entre 1 y 20: "))
    if num1 == num2:
        print("Adivinaste, mi número era %i"%(num1))
        break
    elif num2 < num1:
        print("El número ingresado es menor al número secreto")
    elif num2 > num1:
        print("El número ingresado es mayor al número secreto")

if num1 != num2:
    print("No adivinaste, mi número era %i"%(num1))
        
