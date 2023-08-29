def decodificar(mensaje):
    palabra=[]
    mensaje=mensaje.split(',')
    print(mensaje)
    for i in mensaje:
        decimal=(int(str(i),2))
        letra=(chr(decimal))
        palabra.append(letra)
    mensaje="".join(palabra)
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
    