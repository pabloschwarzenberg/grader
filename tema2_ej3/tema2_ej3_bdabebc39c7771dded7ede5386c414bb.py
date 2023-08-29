def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero


if __name__ == "__main__":
    # Pruebas de la función
    numeros = [6, 28, 12, 496, 20, 15]
    for num in numeros:
        if numero_perfecto(num):
            print(f"{num} es un número perfecto.")
        else:
            print(f"{num} no es un número perfecto.")
