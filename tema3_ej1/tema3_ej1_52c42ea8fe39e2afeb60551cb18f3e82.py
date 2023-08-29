def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    es_primo = suma == 1
    return suma, es_primo


if __name__ == "__main__":
    # Ejemplo de uso
    numero = 12
    suma, es_primo = suma_divisores(numero)



