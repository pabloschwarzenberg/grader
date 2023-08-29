numero = int(input("Ingresa un numero: "))

for i in range(2, numero):
    if numero % i == 0:
        print(i)
