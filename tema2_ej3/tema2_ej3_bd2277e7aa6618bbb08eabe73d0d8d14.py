def numero_perfecto(numero):
    suma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i
    return suma_divisores == numero


if __name__ == "__main__":
    num = int(raw_input("Ingrese un número: "))
    if numero_perfecto(num):
        print("{} es un número perfecto.".format(num))
    else:
        print("{} no es un número perfecto.".format(num))
