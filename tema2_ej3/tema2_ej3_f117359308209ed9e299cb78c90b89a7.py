def numero_perfecto(numero):
    suma_divisores = sum(divisor for divisor in range(1, numero) if numero % divisor == 0)
    return suma_divisores == numero

if __name__ == "__main__":
    numero = int(input("Ingrese un número entero: "))
    es_perfecto = numero_perfecto(numero)

    if es_perfecto:
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")
