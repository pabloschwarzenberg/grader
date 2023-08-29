#SUMA DE LOS DIVISORES DE UN NUMERO
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    es_primo = suma == 1

    return suma, es_primo
