from random import randint
numero = randint(1,20)
vidas = 0
adivinar = True
while adivinar:
    vidas += 1
    if vidas<= 5:
        intento = int(input("Ingrese un numero: "))
        if intento==numero:
            print("Adivinaste, mi número era ",numero)
            adivinar = False
        elif intento>numero:
            print("mi numero es menor")
        elif intento<numero:
            print("mi numero es mayor")
    else:
        adivinar = False
        print("No adivinaste, mi número era ",numero)
        
