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
    num = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(num)
    print("La suma de los divisores de", num, "es:", suma)
    if es_primo:
        print(num, "es primo")
    else:
        print(num, "no es primo")
