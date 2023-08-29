def decodificar(mensaje):
    m=mensaje.split(',')
    k=''
    for i in m:
        k+=chr(int(i[:8],2))
    return k
mensaje=decodificar("01101000,01101111,01101100,01100001")
print(mensaje)
