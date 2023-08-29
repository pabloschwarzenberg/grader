# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    if suma == 1:
        return suma, True  # Si la suma de los divisores es 1, el número es primo
    else:
        return suma, False  # Si la suma de los divisores es distinta de 1, el número no es primo

if __name__ == "__main__":
    # Ejemplos de uso
    numero = 12
    resultado, es_primo = suma_divisores(numero)
    print(f"La suma de los divisores de {numero} es: {resultado}")
    print(f"¿Es {numero} un número primo? {es_primo}")

    numero = 17
    resultado, es_primo = suma_divisores(numero)
    print(f"La suma de los divisores de {numero} es: {resultado}")
    print(f"¿Es {numero} un número primo? {es_primo}")
           