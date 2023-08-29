def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i

    if suma == 1:
        return suma, True
    else:
        return suma, False

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    resultado, es_primo = suma_divisores(num)
    print("La suma de los divisores de", num, "es", resultado)
    if es_primo:
        print(num, "es primo")
    else:
        print(num, "no es primo")

           