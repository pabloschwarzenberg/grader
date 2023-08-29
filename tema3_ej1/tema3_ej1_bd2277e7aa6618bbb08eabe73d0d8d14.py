# completa el código de la función
def suma_divisores(a):
    suma = 0
    es_primo = True

    if a == 1:
        return suma, False

    for i in range(1, a):
        if a % i == 0:
            suma += i
            es_primo = False

    if suma == 1:
        es_primo = True

    return suma, es_primo

if __name__ == "__main__":
    a = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(a)
    print("Suma de los divisores:", suma)
    print("Es primo:", es_primo)
