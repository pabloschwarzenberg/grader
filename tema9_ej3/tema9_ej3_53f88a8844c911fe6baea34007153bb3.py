def decodificar(mensaje):
    conjuntos=mensaje.split(",")
    numeros=[]
    mensajefinal=""
    for x in conjuntos:
        numeros.append(int(x,2))
    for numero in numeros:
        mensajefinal+=chr(numero)

    return mensajefinal

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
