def suma_divisores(numero):
    suma = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    # Prueba de la función con diferentes números
    numeros = [10, 13, 24, 31]

    for numero in numeros:
        suma, es_primo = suma_divisores(numero)
        print(f"Para el número {numero}:")
        print(f"Suma de los divisores: {suma}")
        print(f"¿Es primo?: {es_primo}")
        print()  