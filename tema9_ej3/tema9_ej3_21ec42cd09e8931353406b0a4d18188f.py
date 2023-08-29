def decodificar(mensaje):
    au=mensaje.split(',')
    ka=''
    for i in au:
        ka+=chr(int(i[:8],2))
    return ka
mensaje=decodificar("01101000,01101111,01101100,01100001")
print(mensaje)
