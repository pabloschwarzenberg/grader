def suma_divisores(numero):
    suma = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor
    
    es_primo = suma == 1

    return suma, es_primo

if __name__ == "__main__":
    # Ejemplo de uso
    num = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(num)
    print("Suma de divisores:", suma)
    if es_primo:
        print("El número es primo")
    else:
        print("El número no es primo")
