def numero_perfecto(a):
    suma_divisores = 0

    for divisor in range(1, a):
        if a % divisor == 0:
            suma_divisores += divisor

    return suma_divisores == a


if __name__ == "__main__":
    a = int(input("Ingrese a: "))
    print(numero_perfecto(a))
           