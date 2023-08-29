def decodificar(mensaje):
    lista=mensaje.split(",")
    print(lista)
    decof=[]
    for codigos in lista:
        numeroDecimal= int(codigos,2)
        letra= chr(numeroDecimal)
        decof.append(letra)
    cadena= "".join(decof)
    return cadena

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         