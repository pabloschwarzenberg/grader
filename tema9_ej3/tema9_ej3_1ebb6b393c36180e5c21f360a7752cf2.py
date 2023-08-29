def decodificar(mensaje):
    nuevo = mensaje.split(",")
    mensaje_decodificado = ""
    for caracter in nuevo:
        mensaje_decodificado += chr(int(caracter,2))
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)