def decodificar(mensaje):
    mensaje = "hola"
    codificado = []
    for letra in mensaje:
        codificado.append(ord(letra))
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         