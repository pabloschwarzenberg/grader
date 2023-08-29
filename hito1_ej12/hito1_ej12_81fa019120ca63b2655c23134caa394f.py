#Juego adivina mi número
import random
intentos=0
numero=random.randint(1,20)
print('Piensa un número entre 1 y 20')
while intentos<5:
    intento=int(input('Adivina mi número, éste es tu intento número '+str(intentos+1)+': ')) 
    if intento<numero:
        print('Mi número es mayor')
    if intento>numero:
        print('Mi número es menor')
    if intento==numero or intentos==4:
        break
        
if intento==numero:
    intentos=str(intentos)
    print('Adivinaste, mi número era ',numero)
if intento!=numero:
    numero=str(numero)
    print('No adivinaste, mi número era ',numero)
     