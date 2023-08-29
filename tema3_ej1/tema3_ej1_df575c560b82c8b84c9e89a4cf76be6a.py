# completa el código de la función
def suma_divisores(n):
    suma = 0
    es_primo = True
    if n == 1:
        suma == 0
    for i in range(1,n):
        if n%i == 0:
            suma = suma + i
    if suma == 1:
        es_primo = True
    elif suma != 1:
        es_primo = False

    return suma,es_primo
