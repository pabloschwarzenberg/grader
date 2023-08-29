def suma_divisores(numero):
    suma = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    if suma == 1:
        return suma, True
    else:
        return suma, False

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))

    resultado, es_primo = suma_divisores(numero)

    print("La suma de los divisores de", numero, "es:", resultado)
    print("El número", numero, "es primo:", es_primo)

           