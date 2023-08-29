def numero_perfecto(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    return suma == a

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    if numero_perfecto(numero):
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")
