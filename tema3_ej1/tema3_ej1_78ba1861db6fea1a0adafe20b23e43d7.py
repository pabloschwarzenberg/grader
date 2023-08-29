def suma_divisores(numero):
    suma = 0
    for n in range(1, numero):
        if (numero%n) == 0:
            suma += n

    if suma == 1:
        return suma, True
    else:
        return suma, False

if __name__ == "__main__":
    numero = int(input("Número: "))
    suma, es_primo = suma_divisores(numero)
    print("\nLa suma de sus divisores es:", suma)
    if es_primo:
        print("\nEl número es primo")
    else:
        print("\nEl número no es primo")