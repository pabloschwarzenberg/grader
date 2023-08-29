def decodificar(cod):
    lista = []
    cod = cod.split(sep=',')
    for bi in cod:
        lista.append(bi)
        numeros = []
    for binario in lista:
        cont = len(binario)-1
        suma = 0
        for dig in binario:
            dig = int(dig)
            decimal = dig * (2**cont)
            cont -= 1
            suma += decimal 
        numeros.append(suma)
    l_pal = []
    for numero in numeros:
        l_pal.append(chr(numero))
        palabra = "".join(l_pal)
    return palabra

