def suma_divisores(numero):
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    resultado, primo = suma_divisores(num)
    print("La suma de los divisores es:", resultado)
    print("Es primo:", primo)
