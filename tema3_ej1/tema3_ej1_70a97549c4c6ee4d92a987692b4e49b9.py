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
    a = int(input("Ingrese un número: "))
    suma, primo = suma_divisores(a)
    print("La suma de los divisores es:", suma)
    if primo:
        print("El número", a, "es primo.")
    else:
        print("El número", a, "no es primo.")   