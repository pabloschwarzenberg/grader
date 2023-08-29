def decodificar(mensaje):
    mensaje = mensaje.split(",")
    men_descubierto = ""
    for codigo in mensaje:
        men_descubierto += chr(int(codigo, 2))
    return men_descubierto
         