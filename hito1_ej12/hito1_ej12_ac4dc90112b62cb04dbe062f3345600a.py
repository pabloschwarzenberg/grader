import random
n_secreto=random.randint(1,20)
print(n_secreto)
intentos=0
while intentos<5:
    n_adivinado=int(input("Ingrese un numero del 1 al 20"))
    if (n_adivinado < n_secreto):
        print("Mi numero es mayor")
        intentos=intentos+1
    elif (n_adivinado > n_secreto):
        print("Mi numero es menor")
        intentos=intentos+1
    elif (n_adivinado == n_secreto):
        print("Adivinaste, mi numero era",n_secreto)
if intentos >=5:
    print("No adivinaste, mi numero era",n_secreto)
