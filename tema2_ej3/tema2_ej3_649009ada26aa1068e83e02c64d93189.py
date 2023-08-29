def numero_perfecto(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == numero:
        return True  # Si la suma de los divisores es igual al número, es un número perfecto
    else:
        return False  # Si la suma de los divisores es diferente al número, no es un número perfecto

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    print(numero_perfecto(numero))
