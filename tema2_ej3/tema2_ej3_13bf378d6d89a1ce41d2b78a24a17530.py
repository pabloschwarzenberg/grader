def numero_perfecto(numero):
    suma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    numero_ingresado = int(input("Ingrese un número: "))
    es_perfecto = numero_perfecto(numero_ingresado)

    if es_perfecto:
        print(numero_ingresado, "es un número perfecto.")
    else:
        print(numero_ingresado, "no es un número perfecto.")

          