def numero_perfecto(numero):
    suma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor
    return suma_divisores == numero

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if numero_perfecto(numero):
        print(numero, "es un numero perfecto")
    else:
        print(numero, "no es un numero perfecto")
