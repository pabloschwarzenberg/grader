def numero_perfecto(a):
    return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
def numero_perfecto(numero):
    suma_divisores = 0

    # Iterar desde 1 hasta (numero-1)
    for divisor in range(1, numero):
        # Verificar si es divisor del número
        if numero % divisor == 0:
            suma_divisores += divisor

    # Verificar si la suma de los divisores es igual al número
    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))

    if numero_perfecto(numero):
        print(numero, "es un número perfecto")
    else:
        print(numero, "no es un número perfecto")
          