def decodificar(mensaje):
    lista_mensaje = mensaje.split(",")
    lista = []
    lista2 = []
    for i in lista_mensaje:
        a = int(str(i), 2)
        lista.append(a)
    for i in lista:
        a = chr(i)
        lista2.append(a)

    mensaje = "".join(lista2)

    return mensaje


if __name__ == "__main__":
    mensaje = decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
