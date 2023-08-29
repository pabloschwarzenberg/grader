def suma_divisores(numero):
    suma = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True  # El número es primo
    else:
        return suma, False  # El número no es primo


# Ejemplo de uso
if __name__ == "__main__":
    numero = int(input("Ingrese un número entero: "))
    suma, es_primo = suma_divisores(numero)
    print("Suma de divisores:", suma)
    print("¿Es primo?", es_primo)
