def numero_perfecto(numero):
    suma_divisores = 0

    # Iterar desde 1 hasta el número-1 para encontrar los divisores
    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    # Comprobar si la suma de los divisores es igual al número
    if suma_divisores == numero:
        return True
    else:
        return False

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))

    if numero_perfecto(numero):
        print("El número es perfecto")
    else:
        print("El número no es perfecto")
