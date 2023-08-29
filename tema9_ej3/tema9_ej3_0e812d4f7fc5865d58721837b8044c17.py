def decodificar(mensaje):
    separado = mensaje.split(',')
    print(separado)
    decodificado = ''
    for x in separado:
        decodificado += chr(int(x,2))
    return decodificado


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
