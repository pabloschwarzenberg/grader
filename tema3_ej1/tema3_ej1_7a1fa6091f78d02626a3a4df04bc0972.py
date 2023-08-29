# completa el código de la función
def suma_divisores(numero):
    suma = 0
    es_primo = True

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma != 1:
        es_primo = False

    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado = suma_divisores(numero)
    print(resultado[0])
    print(resultado[1])
