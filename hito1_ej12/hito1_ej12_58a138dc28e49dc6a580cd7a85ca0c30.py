#Juego adivina mi número
numero = int(input("ingresa el numero desde el 1 al 20 por favor: "))
import random
numeros = (1, 20)
intentos = 1
programa = random.randint(1,20)
while programa != numero:
    print("este no es el numero, intentalo de nuevo")    
    if numero != programa and numero > programa:
        print("es mayor")
    if numero < programa and numero != programa:
        print("es menor")
    if intentos == 5:
        print("No adivinaste, mi número era ", programa, )
        break
        numero = int(input("ingresa el numero desde el 1 al 20 por favor: "))
    if programa != numero:
        intentos = intentos + 1  
        
if programa == numero and intentos < 4:
    print("adivinaste, mi numero era: ", programa,)
     