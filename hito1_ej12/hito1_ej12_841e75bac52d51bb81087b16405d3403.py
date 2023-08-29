#Juego adivina mi número
import random

numeroRandom = random.randint(1, 21)
encontrado = False
intentos = 0

while(not encontrado):
        numeroIngresado = int(input("Ingrese número: "))
        
        intentos += 1
    
        if numeroIngresado > numeroRandom:
            print("El número es menor")
    
        elif numeroIngresado < numeroRandom:
            print("El número es mayor")
    
        elif numeroIngresado == numeroRandom:
            encontrado = True
            print("Adivinaste, mi número era ", numeroRandom)
        
        if intentos == 5:
            print("No adivinaste, mi número era ", numeroRandom)
            encontrado = True