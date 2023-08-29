def numero_perfecto(numero):
    suma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))

    if numero_perfecto(numero):
        print("El número", numero, "es perfecto.")
    else:
        print("El número", numero, "no es perfecto.")
