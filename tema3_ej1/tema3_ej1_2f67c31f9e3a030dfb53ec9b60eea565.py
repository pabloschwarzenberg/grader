def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    if suma == 1:
        return suma, True  # Si la suma de los divisores es 1, el número es primo
    else:
        return suma, False

# Ejemplo de uso
if __name__ == "__main__":
    numero = 15
    resultado, es_primo = suma_divisores(numero)
    print("Suma de divisores:", resultado)
    print("¿Es primo?", es_primo)
    