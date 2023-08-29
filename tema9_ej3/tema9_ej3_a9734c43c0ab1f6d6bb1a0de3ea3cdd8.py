def decodificar(mensaje):
    mensaje = mensaje.split(',')
    l_mensaje =list(map(int,mensaje))
    l_numero = []
    for binario in l_mensaje:
        numero = int(str(binario),2)
        l_numero.append(numero)
    l_palabra = []
    for numero in l_numero:
        letra = chr(numero)
        l_palabra.append(letra)
    palabra = ''.join(l_palabra)   
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)

