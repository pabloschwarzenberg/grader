def suma_divisores(numero):
    # Verificar si el número es negativo o cero
    if numero <= 0:
        return None

    # Calcular la suma de los divisores
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    # Determinar si el número es primo
    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    # Solicitar al usuario que ingrese un número entero
    numero = int(input("Ingresa un número entero positivo: "))

    # Llamar a la función para calcular la suma de los divisores y determinar si es primo
    resultado = suma_divisores(numero)

    if resultado is not None:
        suma, es_primo = resultado
        print("La suma de los divisores de", numero, "es:", suma)
        if es_primo:
            print(numero, "es un número primo.")
        else:
            print(numero, "no es un número primo.")
