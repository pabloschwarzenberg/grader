def suma_divisores(numero):
    suma = 0

    # Calcular la suma de los divisores del número
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    # Determinar si el número es primo
    es_primo = suma == 1

    # Retornar la suma de los divisores y si el número es primo o no
    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado, primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", resultado)
    if primo:
        print(numero, "es un número primo")
    else:
        print(numero, "no es un número primo")
