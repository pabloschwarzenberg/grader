#Juego adivina mi número
      
import random

numero_secreto = random.randint(1, 20)
intentos = 5

while intentos > 0:
    n = int(input("Ingrese Numero: "))
    
    if n == numero_secreto:
        print(f"Adivinaste, mi número era {numero_secreto}")
        break
    elif n > numero_secreto:
        print("Mi número es menor")
    elif n < numero_secreto:
        print("Mi número es mayor")
        
    intentos -= 1
    print(f"Te quedan {intentos} intentos.")
        
if intentos == 0:
    print(f"No adivinaste, mi número era {numero_secreto}")
    