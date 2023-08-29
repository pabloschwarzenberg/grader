#Juego adivina mi número
import random
numero = random.randint(1,20)
intentos=0
while intentos<5:
    respuesta = int(input("Cual numero crees que es? "))
    if respuesta==numero:
        print("Adivinaste, mi número era ", numero)
        break
    if respuesta>numero:
        print("mi número es menor")
        intentos= intentos +1
    if respuesta<numero:
        print("mi número es mayor")
        intentos = intentos +1
        
if intentos == 5:
    print("No adivinaste, mi número era", numero )
      