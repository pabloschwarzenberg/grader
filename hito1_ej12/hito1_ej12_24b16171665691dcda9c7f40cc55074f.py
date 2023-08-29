#Juego adivina mi número
import random
variable_a = random.randint(1,20)
variable_b = 0
variable_c = False
while variable_b < 5 :
    variable_c =int(input("ingrese un número:"))
    if variable_c == variable_a :
        print("Adivinaste, mi número era",variable_a)
        break
    if variable_c < variable_a :
        print("El número ingresado es menor")
    if variable_c > variable_a:
        print("El número ingresado es mayor")
    variable_b = variable_b + 1

if variable_b == 5 :
    print("No adivinaste, mi número era",variable_a)    
