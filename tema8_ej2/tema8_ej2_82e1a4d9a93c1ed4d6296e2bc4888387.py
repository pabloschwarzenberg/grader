def buscarTodas(a, b):
    posiciones = ''
    espacios = a.count(b)
    insertados = 1
    for posicion, letra in enumerate(a):
        if b == letra:
            posicion = str(posicion)
            posiciones += posicion
            if insertados <= espacios-1:
                posiciones += ' '
                insertados += 1

    return posiciones