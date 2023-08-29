def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i

    es_primo = suma == 1

    return suma, es_primo
    
numero = 17  # Número de ejemplo
suma, es_primo = suma_divisores(numero)
print("Suma de los divisores:", suma)
print("¿Es primo?", es_primo)

