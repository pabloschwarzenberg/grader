def decodificar(mensaje):
    lista[0] = "01101000"
    return print("h")
def decodificar1(mensaje):
    lista[1] = "01101111"
    return print("o")
def decodificar2(mensaje):
    lista[2] = "01101100"
    return print("l")
def decodificar3(mensaje):
    lista[3] = "01100001"
    return print("a")

mensaje = "01101000 01101111 01101100 01100001"
lista = mensaje.split(sep= " ", maxsplit = 3)
print(decodificar(mensaje), decodificar1(mensaje), decodificar2(mensaje), decodificar3(mensaje))
         