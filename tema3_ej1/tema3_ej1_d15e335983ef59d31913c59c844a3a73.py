# completa el código de la función
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
    num = int(input("Introduce un número: "))
    suma, es_primo = suma_divisores(num)
    print("La suma de los divisores de", num, "es", suma)
    if es_primo:
        print(num, "es un número primo")
    else:
        print(num, "no es un número primo")