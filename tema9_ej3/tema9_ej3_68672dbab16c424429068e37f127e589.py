def decodificar(mensaje):
    n=""
    a=mensaje.split(",")
    for c in a:
       n+=chr(int(str(c), 2))
    return n