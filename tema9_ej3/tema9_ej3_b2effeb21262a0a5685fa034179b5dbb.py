def decodificar(mensaje):
    mensaje =mensaje.split(',')
    m=''
    for i in mensaje:
        decimal=0
        for posicion, digito_string in enumerate(i[::-1]):
            decimal += int(digito_string) * 2 ** posicion
        m=m+chr(decimal)

    return m

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         