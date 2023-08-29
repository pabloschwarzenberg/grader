def decodificar(mensaje):
    mensaje = mensaje.split(",")
    lista = []
    for secuencia in mensaje:
        secuencia = (int(secuencia,2))
        secuencia = chr(secuencia)
        lista.append(secuencia)
    mensaje = "".join(lista)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         