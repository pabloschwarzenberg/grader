def numero_perfecto(numero):
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    return suma_divisores == numero

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))

    if numero_perfecto(numero):
        print(numero, "es un número perfecto.")
    else:
        print(numero, "no es un número perfecto.")

           