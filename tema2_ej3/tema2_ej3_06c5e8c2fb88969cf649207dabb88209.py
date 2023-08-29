def numero_perfecto(numero):
    suma_divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma_divisores += divisor

    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado = numero_perfecto(numero)
    if resultado:
        print("El número", numero, "es perfecto.")
    else:
        print("El número", numero, "no es perfecto.")
          