def decodificar(mensaje):
    num_bin=mensaje.split(",")
    letras=[chr(int(binario, 2)) for binario in num_bin]
    mensaje_dec="".join(letras)
    return mensaje_dec

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         