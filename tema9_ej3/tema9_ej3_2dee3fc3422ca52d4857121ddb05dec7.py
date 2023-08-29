def decodificar(mensaje):
    mensaje=mensaje.split(",")
    m=""
    for x in mensaje:
        try:
            octetos = bytearray(int(y, 2) for y in x.split())
        except:
            print('No es una cadena binaria.')
            pass
        try:
            m+=octetos.decode(encoding='utf8')
        except:
            print('No es una cadena codificada')
            pass
    return m

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         