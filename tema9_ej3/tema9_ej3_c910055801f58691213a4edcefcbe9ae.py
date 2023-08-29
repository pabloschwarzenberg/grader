def decodificar(mensaje):
    a = mensaje.split(",")
    lista = []
    for num in a:
        nom = int(num,2)
        lista.append(chr(nom))
    return "".join(lista)
         