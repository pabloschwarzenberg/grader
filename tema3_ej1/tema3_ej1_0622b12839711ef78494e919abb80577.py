def suma_divisores(numero):
    suma = 0
    es_primo = True

    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    if suma != 1:
        es_primo = False

    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    resultado_suma, resultado_es_primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", resultado_suma)
    print("El número", numero, "es primo:", resultado_es_primo)