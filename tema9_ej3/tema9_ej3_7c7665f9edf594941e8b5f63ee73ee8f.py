def decodificar(mensaje):
    numbin = mensaje.split(',')
    decimal = []
    decod = ''
    for i in numbin:
        decimal.append(int(i, 2))
    for c in decimal:
        caracter = chr(c)
        decod = decod + caracter
    return decod

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         