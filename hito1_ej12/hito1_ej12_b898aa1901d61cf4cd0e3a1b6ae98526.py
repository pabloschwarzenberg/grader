#Juego adivina mi número
import random
it = 1
numero = random.randint(1,20)
if __name__ == "__main__":
    while it < 6:
        print("Ingrese un número")
    
        a=input()
        a=int(a)
        if a < numero:
            print("mi número es mayor")
            it+=1
        if a > numero:
            print("mi número es menor")
            it+=1
        if a == numero:
            break
    if a == numero:
        print("Adivinaste, mi número era", numero)
    else:
        print("No adivinaste, mi número era", numero)
    