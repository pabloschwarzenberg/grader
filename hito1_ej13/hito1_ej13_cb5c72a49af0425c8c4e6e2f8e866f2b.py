# Primos

numero = int(input("Ingrese un numero: "))

print("\nFactores primos de " + str(numero) + " (No se incluye el 1 ni el mismo numero)")
for i in range(2, numero):
    while True:
        if numero % i == 0:
            numero = numero / i
            print(i)
        else:
            break 