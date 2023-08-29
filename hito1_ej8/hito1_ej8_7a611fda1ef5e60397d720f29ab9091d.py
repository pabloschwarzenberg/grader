#Descomponer un número
def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    if miles > 0:
        print(miles, "M", end=" + ")
    if centenas > 0 or miles > 0:
        print(centenas, "C", end=" + ")
    if decenas > 0 or centenas > 0 or miles > 0:
        print(decenas, "D", end=" + ")
    print(unidades, "U", end="")

numero = int(input("Ingresa un número de hasta 4 dígitos: "))
descomponer_numero(numero)