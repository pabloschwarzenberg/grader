def decodificar(mensaje):
    mensaje=mensaje.split(",")
    lista=[]
    lista2=[]
    for f in mensaje:
        num=int(str(f),2)
        lista.append(num)
    for a in lista:
        s=chr(a)
        lista2.append(s)
    return("".join(lista2))

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         