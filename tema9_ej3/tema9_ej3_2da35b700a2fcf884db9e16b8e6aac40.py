def decodificar(mensaje):
    listaCaracteres = mensaje.split(",")
    mensaje = ""
    for item in listaCaracteres:
        mensaje += chr(int(item, base=2))
    return mensaje


         