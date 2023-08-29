def decodificar(mensaje):
    lista = mensaje.split(',')
    lista_2 = []
    for i in lista:
        traduccion = int(i, 2)
        letra = chr(traduccion)
        lista_2.append(letra)
    resultado = ''
    for j in lista_2:
        resultado += j
    return resultado