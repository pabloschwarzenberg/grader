def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número entero: "))
    resultado, es_primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", resultado)
    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")
