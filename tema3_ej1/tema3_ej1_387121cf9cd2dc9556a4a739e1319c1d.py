# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i

    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    resultado, primo = suma_divisores(numero)
    print("La suma de los divisores de", numero, "es:", resultado)
    print("El número", numero, "es primo:", primo)
