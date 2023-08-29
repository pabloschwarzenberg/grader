def decodificar(mensaje):
    mensaje_binario = mensaje.split(",")
    mensaje = ""
    for binario in mensaje_binario:
        decimal = int(binario, 2)
        letra = chr(decimal)
        mensaje = mensaje + letra
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         