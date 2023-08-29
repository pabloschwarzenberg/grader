def numero_perfecto(n):
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

if __name__ == "__main__":
    num = int(input("Introduce un número: "))
    if numero_perfecto(num):
        print("{} es un número perfecto".format(num))
    else:
        print("{} no es un número perfecto".format(num))