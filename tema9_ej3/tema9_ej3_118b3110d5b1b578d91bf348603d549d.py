def decodificar(mensaje):
    mensaje = list(mensaje)
    mensaje.append(",")
    lista_mensaje = []
    k = ""
    for i in mensaje:
        k += i
        if i == ",":
            k = list(k)
            k.remove(",")
            lista_mensaje.append(k)
            k= ""
    q = ""
    letra = ""
    for i in range(len(lista_mensaje)):
        for j in lista_mensaje[i]:
            q += j
        dec = int(str(q),2)
        asci = chr(dec)
        letra += asci
        q = ""
    return letra

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)