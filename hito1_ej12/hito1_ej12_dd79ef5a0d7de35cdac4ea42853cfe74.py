import random
intentos_realizados=0
numero=random.randint(1,20)

while intentos_realizados<6:
    numero_estimado=int(input("Ingresa numero: "))
    if numero_estimado==numero:
        print("Adivinaste, mi numero era ", numero)
        break
    else:
        intentos_realizados=intentos_realizados+1
        if numero_estimado<numero:
            print("Mi numero es mayor")
        if numero_estimado>numero:
            print("Mi numero es menor")
        if intentos_realizados==5:
            print("No adivinaste, mi numero era ",numero)
            break