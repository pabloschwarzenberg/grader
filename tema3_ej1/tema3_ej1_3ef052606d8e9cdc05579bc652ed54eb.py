# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    es_primo = suma == 1

    return suma, es_primo


if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    resultado_suma, es_primo = suma_divisores(num)
    print("Suma de los divisores:", resultado_suma)
    print("El número es primo:", es_primo)

           