def decodificar(mensaje):
    separar = mensaje.split(",")
    texto =""
    for separar in separar:
        cod = int(separar,2)
        letra = chr(cod)
        texto=texto+letra
    return texto

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         