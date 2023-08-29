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
    # Solicitar el número al usuario
    numero = int(input("Ingresa un número: "))

    # Verificar si el número es perfecto
    es_perfecto = numero_perfecto(numero)

    # Imprimir el resultado
    if es_perfecto:
        print(numero, "es un número perfecto")
    else:
        print(numero, "no es un número perfecto")           