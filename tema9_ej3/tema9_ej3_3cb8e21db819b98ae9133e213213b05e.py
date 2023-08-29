def decodificar(mensaje):
    binarios = mensaje.split(",")
    caracteres = [chr(int(binarios, 2)) for binarios in binarios]
    mensaje_decodificado = "".join(caracteres)
    return mensaje_decodificado

if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
