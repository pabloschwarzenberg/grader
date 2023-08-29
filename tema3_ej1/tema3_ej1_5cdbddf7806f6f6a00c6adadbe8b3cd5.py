def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
    return suma, suma == 1

if __name__ == "__main__":
    num = 12
    suma, es_primo = suma_divisores(num)
    print("La suma de los divisores de {num} es: {suma}")
    if es_primo:
        print("{num} es un número primo.")
    else:
        print("{num} no es un número primo.")



           