import random as rnd
x = rnd.randrange(20)
i = 1
n = 5

def juego(j):
    if j > x:
        return("Mi número es menor")
    elif j < x:
        return("Mi número es mayor")
    elif j == x:
        return("Adivinaste, mi número era " + str(x))


while i <= n:
    j = int(input("Ingrese un número: "))
    print(juego(j))
    if i == n and j != x:
        print("No adivinaste, mi número era " +str(x))
    elif j == x:
        break
    i += 1


