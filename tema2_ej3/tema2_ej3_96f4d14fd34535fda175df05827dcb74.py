def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero


if __name__ == "__main__":
    # Ejemplos de uso
    print(numero_perfecto(6))  # True
    print(numero_perfecto(28))  # True
    print(numero_perfecto(12))  # False

           