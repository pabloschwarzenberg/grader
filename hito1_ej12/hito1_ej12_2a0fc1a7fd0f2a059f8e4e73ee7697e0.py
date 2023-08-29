import random

# Generar número aleatorio
secreto = random.randint(1, 20)

print("Adivina mi número entre 1 y 20. Tienes 5 intentos.")

# Ciclo para los 5 intentos
for i in range(5):
    intento = int(input("Intento {}: ".format(i+1)))
    
    if intento == secreto:
        print("Adivinaste, mi número era", secreto)
        break
    elif intento < secreto:
        print("Mi número es mayor")
    else:
        print("Mi número es menor")
else:
    print("No adivinaste, mi número era", secreto)