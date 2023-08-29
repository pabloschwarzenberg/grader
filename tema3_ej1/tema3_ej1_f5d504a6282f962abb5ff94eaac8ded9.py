
def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i

    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado, primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", resultado)
    print("El número", numero, "es primo:", primo)     