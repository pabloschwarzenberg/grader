def decodificar(mensaje):
    lista_mensaje=mensaje.split(",")
    lista_1=[]
    for i in lista_mensaje:
        lista_1.append(chr((int(str(i), 2))))
    mensaje_final="".join(lista_1)
    return mensaje_final

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         