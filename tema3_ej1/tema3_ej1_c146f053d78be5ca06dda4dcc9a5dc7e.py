def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    # Solicitar al usuario ingresar un número entero
    numero = int(input("Ingrese un número: "))

    # Calcular la suma de los divisores y si el número es primo o no
    suma, es_primo = suma_divisores(numero)

    # Imprimir el resultado
    print("Suma de divisores:", suma)
    print("¿Es primo?", es_primo)
           