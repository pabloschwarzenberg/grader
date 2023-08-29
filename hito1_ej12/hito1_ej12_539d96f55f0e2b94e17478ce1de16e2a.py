from random import randint
numero_para_adivinar=randint(1,20)
intentos=0
numero_acertado=0
while intentos<=5:
    if intentos>1:
        numero_acertado=int(input("intenta denuevo: "))
    else:
        numero_acertado=int(input("digita el numeri que crees que tengo: "))
    intentos+=1
    if numero_acertado==numero_para_adivinar:
        print("adivinaaste, mi numero era", numero_para_adivinar)
        break
    if numero_para_adivinar>numero_acertado:
        print("mi numero es mayor")
    else:
        print("mi numero es menor")
    if intentos==5:
        print("no adivinaste, mi numero era", numero_para_adivinar)
        break