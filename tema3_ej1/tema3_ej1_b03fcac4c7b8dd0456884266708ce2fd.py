# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo


if __name__ == "__main__":
    a = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(a)
    print("La suma de los divisores de", a, "es:", suma)
    if es_primo:
        print(a, "es un número primo.")
    else:
        print(a, "no es un número primo.")
           