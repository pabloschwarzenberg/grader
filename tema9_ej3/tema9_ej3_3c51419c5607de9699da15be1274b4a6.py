def lista_string(lista):
    strs = "".join(lista)
    return strs

def string_lista(strs):
    lista = []
    for i in strs:
        lista.append(i)
    return lista

def decodificar(mensaje):
    mensaje = mensaje.split(",")
    mensaje1 = []
    for i in mensaje:
        i = int(i,2)
        mensaje1.append(i)
    mensaje2 = []
    for i in mensaje1:
        i = chr(i)
        mensaje2.append(i)
    mensaje2 = lista_string(mensaje2)
    return mensaje2

