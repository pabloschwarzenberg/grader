# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    if suma == 1:
        return suma, True  # Retorna la suma de divisores y True si el número es primo
    else:
        return suma, False  # Retorna la suma de divisores y False si el número no es primo

if __name__ == "__main__":
    num = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(num)
    print("Suma de los divisores:", suma)
    print("¿Es primo?", es_primo)           