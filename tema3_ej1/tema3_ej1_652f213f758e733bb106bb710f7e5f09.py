def suma_divisores(numero):
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True  # Retorna la suma y True si el número es primo
    else:
        return suma, False  # Retorna la suma y False si el número no es primo


if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))

    resultado, es_primo = suma_divisores(numero)

    print("La suma de los divisores de", numero, "es:", resultado)

    if es_primo:
        print(numero, "es un número primo")
    else:
        print(numero, "no es un número primo")
