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
    num = int(input("Ingresa un número: "))
    div_sum, es_primo = suma_divisores(num)
    print("La suma de los divisores de", num, "es:", div_sum)
    if es_primo:
        print(num, "es un número primo.")
    else:
        print(num, "no es un número primo.")
