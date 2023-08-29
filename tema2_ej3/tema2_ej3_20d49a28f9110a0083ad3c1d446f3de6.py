def numero_perfecto(Numero):
    suma_divisores = 0
    for divisor in range(1, Numero):
        if Numero % divisor == 0:
            suma_divisores += divisor
    return suma_divisores == Numero
if __name__ == "__main__":
    Numero = int(input("Ingrese un número: "))
    if numero_perfecto(Numero):
        print("El número es perfecto")
    else:
        print("El número no es perfecto")