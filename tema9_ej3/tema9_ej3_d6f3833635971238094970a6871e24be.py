def decodificar(mensaje):
    mensaje = ("01101000,01101111,01101100,01100001")
    h = (mensaje[0:8])
    o = (mensaje[9:17])
    l = (mensaje[18:26])
    a = (mensaje[27:35])
    lista = []
    lista.append(h)
    lista.append(o)
    lista.append(l)
    lista.append(a)
    lista2 = []
    lista3 = []
    for i in lista:
        d =int(i,2)
        lista2.append(d)
    for j in lista2:
        c = chr(int(j))
        lista3.append(c)

    mensaje ="".join(lista3)
        
    return mensaje

if __name__ == "__main__":
    mensaje=decodificar("01101000,01101111,01101100,01100001")
    print(mensaje)
