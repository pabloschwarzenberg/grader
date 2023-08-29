# Importar
import random   

# Cte
number = random.randint(1,20)

# Entrada
x = 0
intentos = 5
# Procesamiento
while intentos > 0:
    x = int(input("qué numero estoy pensando?: "))
    if x < number:
        print("Mi número es mayor")
        print("Te quedan {} intentos.".format(intentos))
        intentos -= 1
    else: 
        print("Mi número es menor")
        print("Te quedan {} intentos.".format(intentos))
        intentos -= 1

    if x == number:
        print("Adivinaste mi número!, mi número era {}".format(number))
        exit()