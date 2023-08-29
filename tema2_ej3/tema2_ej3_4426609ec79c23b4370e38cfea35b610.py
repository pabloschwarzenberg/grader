def numero_perfecto(a):
    suma = 0
    dividir = a
    while dividir > 1:
        dividir = dividir - 1
        if (a % dividir) == 0:
            suma += dividir
    m = False
    if suma == a:
        m = True

    return m
