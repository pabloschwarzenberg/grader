def decodificar(mensaje):
    mensaje=str(mensaje)
    mensaje=mensaje.split(",")
    palabra=[]
    for i in mensaje:
        i=int(i,2)
        i=chr(i)
        i=str(i)
        palabra.append(i)
    palabra="".join(palabra)
    return palabra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         