def decodificar(mensaje):
    nuevo_mensaje=mensaje.split(",")
    lista=[]
    mensaje=""
    mensajefinal=""
    for elemento in nuevo_mensaje:
        for k in range(len(elemento)):
            numero=(int(elemento[k])*2**(7-int(k)))
            lista.append(numero)
        suma=sum(lista)
        mensaje=mensaje+chr(suma)
        lista.clear()
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
         