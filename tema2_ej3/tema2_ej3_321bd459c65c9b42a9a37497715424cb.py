def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    return suma_divisores == numero

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(num)
    if es_perfecto:
        print(num, "es un número perfecto.")
    else:
        print(num, "no es un número perfecto.")

           