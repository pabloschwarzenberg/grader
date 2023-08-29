num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

menor = num1
medio = num2
mayor = num3

while not (menor <= medio <= mayor):
    if menor > medio:
        menor, medio = medio, menor
    if medio > mayor:
        medio, mayor = mayor, medio

print("Números ordenados: {}, {}, {}".format(menor, medio, mayor))