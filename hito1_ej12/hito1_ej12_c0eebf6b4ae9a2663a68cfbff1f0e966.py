import random
n = random.randint(1,20)
intentos = 5
while True:
    numero = int(input("Introduce un numero entre 1 y 20: "))
    if numero < n:
        print(">>tu numero es mayor que el buscado")
    if numero > n:
        print(">>tu numero es menor que el buscado")
    if numero == n:
        print("Adivinaste, mi número era",n)
        break
    if numero != n:
        intentos -=1
    if intentos ==0:
        print("No adivinaste, mi número era",n)
        break