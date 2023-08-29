def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma, suma == 1

if __name__ == "__main__":
    numero = int(input("Ingresa un número: "))
    suma, es_primo = suma_divisores(numero)

    print("La suma de los divisores de", numero, "es", suma)
    if es_primo:
        print(numero, "es un número primo.")
    else:
        print(numero, "no es un número primo.")
           