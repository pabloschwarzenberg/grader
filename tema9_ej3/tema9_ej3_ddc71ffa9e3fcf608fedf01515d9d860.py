def decodificar(mensaje):
    numerosbinarios = mensaje.split(",")
    letras = [chr(int(binario, 2)) for binario in numerosbinarios]
    decodificado = "".join(letras)
    return decodificado

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)