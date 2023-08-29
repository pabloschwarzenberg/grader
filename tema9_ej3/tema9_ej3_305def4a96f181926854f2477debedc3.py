def decodificar(mensaje):
    palabra = mensaje.split(',')
    mensaje = ''
    for i in palabra:
        x = 0
        for y in i:
            x = x * 2 + int(y)
            mensaje += chr(x)
    return mensaje
         