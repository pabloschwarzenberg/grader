def decodificar(mensaje):
    caracteres = ""
    aux = ""
    for c in mensaje:
        if c!= ',':
            aux += c
        else:
            caracteres += chr(int(aux,2))
            aux = ""
    caracteres += chr(int(aux,2))
    return caracteres
if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         