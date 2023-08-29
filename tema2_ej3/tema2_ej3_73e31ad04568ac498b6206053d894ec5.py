def numero_perfecto(n):
    suma_divisores = 0
    for i in range(1, n):
        if n % i == 0:
            suma_divisores += i
    return suma_divisores == n

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    if numero_perfecto(num):
        print("El número", num, "es perfecto.")
    else:
        print("El número", num, "no es perfecto.")