#Juego adivina mi número
intentos=5
n=int(input())
for s in range (1,20):
    if 0<intentos <=5:
        if n < s:
            print("mi número es menor")
        elif n>s:
            print("mi número es mayor")
        else:
            print("Adivinaste, mi número era: ", n)
            break
    intentos = intentos-1
    
     