def suma_divisores(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    if suma == 1:
        return suma, True
    else:
        return suma, False

if __name__ == "__main__":
    n = int(input("Ingrese un número: "))
    s, es_primo = suma_divisores(n)
    print("La suma de los divisores de", n, "es", s)
    if es_primo:
        print(n, "es primo")
    else:
        print(n, "no es primo")