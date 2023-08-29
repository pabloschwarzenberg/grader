def numero_perfecto(num):
    suma_divisores = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            suma_divisores += divisor
    return suma_divisores == num
if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    if numero_perfecto(num):
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
