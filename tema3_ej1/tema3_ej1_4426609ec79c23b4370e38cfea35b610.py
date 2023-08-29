# completa el código de la función
def suma_divisores(a):
    suma = 0
    dividir = a
    while dividir > 1:
        dividir = dividir - 1
        if (a % dividir) == 0:
            suma += dividir
    m = False
    if suma == 1:
        m = True

    return suma,m           