def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    es_primo = (suma == 1)
    return suma, es_primo

if __name__ == "__main__":
    n = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(n)
    print("Suma de divisores:", suma)
    print("Es primo:", es_primo)
