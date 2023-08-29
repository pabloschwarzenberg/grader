# completa el código de la función
def suma_divisores(n):
    suma = 0
    for j in range(1, n):
        if n % j == 0:
            suma += j    
    es_primo = suma == 1
    return suma, es_primo

           