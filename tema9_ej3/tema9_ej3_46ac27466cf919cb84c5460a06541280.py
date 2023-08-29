def decodificar(mensaje):
    decodificar = mensaje.split(',')
    decodificado = ''
    i = 0
    while i < len(decodificar):
        decimal = int(decodificar[i],2)
        decodificado += chr(decimal)
        i += 1
    return decodificado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
    pass
#int(binario,2)
         