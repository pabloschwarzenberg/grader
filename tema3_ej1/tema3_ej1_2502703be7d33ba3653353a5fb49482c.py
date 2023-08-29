# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(num)
    print("La suma de los divisores de", num, "es:", suma)
    if es_primo:
        print(num, "es un número primo.")
    else:
        print(num, "no es un número primo.")

           