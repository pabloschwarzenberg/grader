# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(numero)

    print("Suma de divisores:", suma)
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")

           