#Juego adivina mi número
print("Hola jugador(a)")
import random
resultado = random.randint(1, 20)
while True:
    adivinar = resultado
    num = int(input("Ingrese un numero: "))   
    if num == adivinar:
        print("Adivinaste, mi número era ", adivinar)
    if num != adivinar:
        if num > adivinar:
            print("mi número es menor")
        if num < adivinar:
            print("mi número es mayor")
        print("Intento N°2")
        num = int(input("Ingrese un numero: "))
        if num != adivinar:
            if num > adivinar:
                print("mi número es menor")
            if num < adivinar:
                print("mi número es mayor")
            print("Intento N°3")
            num = int(input("Ingrese un numero: "))
            if num != adivinar:
                if num > adivinar:
                    print("mi número es menor")
                if num < adivinar:
                    print("mi número es mayor")
                print("Intento N°4")
                num = int(input("Ingrese un numero: "))
                if num != adivinar:
                    if num > adivinar:
                        print("mi número es menor")
                    if num < adivinar:
                        print("mi número es mayor")
                    print("Intento N°5")
                    print("No adivinaste mi número era ",adivinar)
                    break
      