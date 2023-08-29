#Juego adivina mi número
import random
def resultado(x,y):
    if x < y:
        print("mi número es menor")
    elif x > y:
        print("mi número es mayor")
    elif x == y:
        print("Adivinaste, mi número era: ", x)
    return
contador = 0
A = random.randint(0,20)
print(A)
while True:
    contador = contador + 1
    if contador <6 :
        B = int(input("Adivine el Número del 1 al 20: "))
        c=resultado(A,B)
        if A==B:
            break
    else:
        print("No adivinaste, mi número era: ",A)
        break