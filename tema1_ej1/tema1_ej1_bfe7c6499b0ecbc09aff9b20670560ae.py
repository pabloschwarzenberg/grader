#Suma de los N primeros números
import random
adivinar = ""
for i in range(4):
    posible= random.randint(0,9)
    while str(posible) in adivinar:
        posible= random.randint(0,9)
    adivinar+=str(posible)
adivinado =input("Ingrese el número que desea encontrar: ")
intentos = 1
while adivinado != adivinar:
    intentos+=1
    fama = 0
    toque = 0
    for i in range(4):
        if adivinar[i] == adivinado[i]:
            fama+=1
        elif adivinar[i] in adivinado:
            toque+=1
    print(f"tu número tiene fama y {toque} toque",{fama})
    adivinado = input("Escribe otro número: ")
 
print (f"Felicitaciones! Adivinaste el código en {intentos} intentos.")