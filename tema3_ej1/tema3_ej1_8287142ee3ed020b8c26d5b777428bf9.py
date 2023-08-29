# completa el código de la función
def suma_divisores(numero):
    suma = 0

    # Calculamos la suma de los divisores del número
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    # Determinamos si el número es primo o no
    es_primo = suma == 1

    # Retornamos la suma de los divisores y si el número es primo o no
    return suma, es_primo

if __name__ == "__main__":
    # Ejemplo de uso
    numero = int(input("Ingrese un número: "))
    resultado_suma, resultado_es_primo = suma_divisores(numero)
    print("Suma de los divisores:", resultado_suma)
    print("Es primo:", resultado_es_primo)