# completa el código de la función
def suma_divisores(numero):
    suma = 0

    # Iterar desde 1 hasta número-1
    for i in range(1, numero):
        # Verificar si i es divisor de numero
        if numero % i == 0:
            suma += i

    # Determinar si el número es primo o no
    es_primo = suma == 1

    # Retornar la suma de los divisores y si el número es primo o no
    return suma, es_primo

           