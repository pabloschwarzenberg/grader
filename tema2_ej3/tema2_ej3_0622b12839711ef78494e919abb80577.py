def numero_perfecto(numero):
    suma_divisores = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor

    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(numero)

    if es_perfecto:
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")
