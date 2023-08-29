def decodificar(mensaje):
    mensaje_codificado = mensaje.split(",")
    mensaje_decodificado = ""
    for binario in mensaje_codificado :
        decimal = int(binario, 2)
        caracter = chr(decimal)
        mensaje_decodificado += caracter
        mensaje = mensaje_decodificado
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         