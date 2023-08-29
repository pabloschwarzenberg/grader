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
    numero_ingresado = int(input("Ingresa un número: "))
    suma, es_primo = suma_divisores(numero_ingresado)
    print("La suma de los divisores de", numero_ingresado, "es:", suma)
    if es_primo:
        print(numero_ingresado, "es un número primo.")
    else:
        print(numero_ingresado, "no es un número primo.")

           