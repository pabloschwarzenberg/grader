def decodificar(mensaje):
    m=mensaje.split(',')
    r=''
    for i in m:
        r+=chr(int(i[:8],2))
    return r
mensaje=decodificar("01101000,01101111,01101100,01100001")
print(mensaje)