import random 
num_aleatorio = random.randint(1,120)
print(num_aleatorio)
contador = 0

while contador < 5:
    num = int(input("Ingrese un número"))
    if(num < num_aleatorio):
        print("El número ingresado es menor")
    elif(num > num_aleatorio):
        print("El número ingresado es mayor")
    elif(num == num_aleatorio):
        print("Adivinaste, mi número era:", num_aleatorio)
        break
    contador +=1
    print("Intento:", contador, "fallido")

if(num != num_aleatorio):
    print("No adivinaste, mi número era", num_aleatorio)