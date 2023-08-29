# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    # Ejemplo de uso
    numero = int(input("Ingrese un número: "))
    resultado = suma_divisores(numero)
    print("La suma de los divisores es:", resultado[0])
    print("Es primo:", resultado[1])
