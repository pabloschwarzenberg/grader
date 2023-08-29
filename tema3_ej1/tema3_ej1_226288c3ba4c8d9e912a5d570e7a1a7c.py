def suma_divisores(numero):
    # Inicializar la suma de los divisores
    suma = 0

    # Iterar desde 1 hasta número-1 para encontrar los divisores
    for i in range(1, numero):
        # Verificar si i es divisor de número
        if numero % i == 0:
            # Sumar el divisor a la suma
            suma += i

    # Determinar si el número es primo o no
    es_primo = suma == 1

    # Retornar la suma de los divisores y si el número es primo o no
    return suma, es_primo

if __name__ == "__main__":
    # Pedir al usuario que ingrese un número
    numero = int(input("Ingrese un número: "))

    # Llamar a la función para obtener la suma de los divisores y si es primo o no
    resultado = suma_divisores(numero)

    # Imprimir el resultado
    print("La suma de los divisores de", numero, "es:", resultado[0])
    print("El número", numero, "es primo:", resultado[1])