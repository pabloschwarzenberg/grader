def decodificar(mensaje):
    nuevoTexto = mensaje.split(",")
    numerosDecimales = []
    for bit in nuevoTexto:
        i=0
        largo= len(bit)-1
        sumas=0
        while i < len(bit):
            sumas= sumas + (int(bit[i])*(2**largo))
            i+=1
            largo-=1
        numerosDecimales.append(sumas)
    palabra = ""
    for numero in numerosDecimales:
        caracter = chr(numero)
        palabra += caracter

    return palabra