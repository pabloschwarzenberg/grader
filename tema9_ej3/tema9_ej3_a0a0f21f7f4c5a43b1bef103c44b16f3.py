def decodificar(mensaje):
    lista = []
    mensaje = mensaje.split(",")
    for i in mensaje:
        lista.append(int(str(i),2))
    lista2= []
    for i in lista:
        lista2.append(chr(i))
    palabra = ""
    for i in lista2:
        palabra+=i
    return palabra