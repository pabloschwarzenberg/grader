def numero_perfecto(num):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    return suma_divisores == num

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if numero_perfecto(numero):
        print("{numero} es un número perfecto.")
    else:
        print("{numero} no es un número perfecto.")

