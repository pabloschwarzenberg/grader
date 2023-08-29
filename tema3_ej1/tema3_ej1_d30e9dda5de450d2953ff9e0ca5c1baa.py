def suma_divisores(numero):
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True
    else:
        return suma, False

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    suma, es_primo = suma_divisores(numero)
    print("La suma de los divisores es:", suma)
    print("El número es primo:", es_primo)