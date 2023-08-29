#Juego adivina mi número
from random import randint

ns = randint(1,20)

ad = 0

for i in range(5):
    n = int(input("Ingresa un numero: "))
    if n < ns:
        print("EL NUMERO ES MENOR QUE EL NUMERO SECRETO")
    elif n > ns:
        print("EL NUMERO ES MAYOR QUE EL NUMERO SECRETO")
    elif n == ns:
        ad += 1
        break

if ad == 1:
    print("Adivinaste, mi número era", ns)
else:
    print("No adivinaste, mi número era", ns)