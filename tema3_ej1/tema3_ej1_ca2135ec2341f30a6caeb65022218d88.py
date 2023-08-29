def suma_divisores(numero):
    suma = 0

    # Calcular la suma de los divisores
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    # Determinar si el número es primo
    es_primo = suma == 1

    # Devolver la suma de los divisores y si el número es primo o no
    return suma, es_primo

if __name__ == "__main__":
    # Solicitar el número al usuario
    numero = int(input("Ingrese un número: "))

    # Calcular la suma de los divisores y si el número es primo o no
    resultado_suma, resultado_primo = suma_divisores(numero)

    # Imprimir los resultados
    print("La suma de los divisores de", numero, "es:", resultado_suma)
    if resultado_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")
           