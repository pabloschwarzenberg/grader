#Juego adivina mi número
import random
numero_rondom = random.randint(10,20)
variable_one = 5
variable_two = 1
numero_ingresado = int(input("ingresa un numero: "))

while (numero_ingresado != numero_rondom) and (variable_one>1):
    if(numero_ingresado>numero_rondom):
        print("ingresa un numero menor")
    elif (numero_ingresado<numero_rondom):
        print("ingresa un numero mayor")
    variable_one = variable_one - 1
    variable_two = variable_two + 1
    print("te quedan" , numero_ingresado , "intentos")
    numero_ingresado = int(input("ingresa un numero: "))
    
if (numero_ingresado == numero_rondom):
    print("Adivinaste, mi numero era", numero_rondom)
else:
    print("No adivinaste, mi numero y era", numero_rondom)      