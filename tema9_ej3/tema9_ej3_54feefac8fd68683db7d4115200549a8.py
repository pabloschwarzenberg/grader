def decodificar(mensaje):
    a = str(mensaje[0:9])
    decimal1 = (str(a), 2)
    letra1 = chr.decimal1
    b = str(mensaje[10:17])
    decimal2 = (str(b), 2)
    letra2 = chr.decimal2
    c = str(mensaje[19:26])
    decimal3 = (str(c), 2)
    letra3 = chr.decimal3
    d = str(mensaje[28:35])
    decimal4 = (str(d), 2)
    letra4 = chr.decimal4
    palabra= letra1+letra2+letra3+letra4
    return hola