def suma_divisores(a):
    suma = 0

    for i in range(1, a):
        if a % i == 0:
            suma += i

    if suma == 1:
        es_primo = True
    else:
        es_primo = False

    return suma, es_primo

if __name__ == "__main__":
    a = int(input("Ingresa un número entero positivo: "))
    resultado, primo = suma_divisores(a)

    print("La suma de los divisores de {a} es: {resultado}")
    print("El número {a} {'es primo' if primo else 'no es primo'}")

           