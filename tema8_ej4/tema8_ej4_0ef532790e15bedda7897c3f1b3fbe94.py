def rot13(palabra):
    nuevapalabra=""
    for x in palabra:
        ordx=ord(x)
        if (ordx > 90 and ordx < 97) or ordx < 65 or ordx > 122:
            nuevapalabra=nuevapalabra+(x)
        else:
            if str():
                asciirange = 91
                aciibound = 65
            else:
                asciirange = 123
                aciibound = 97
        nuevax= (ordx+13)%asciirange
        if nuevax < aciibound:
            nuevax = nuevax + aciibound
            nuevapalabra=nuevapalabra+chr(nuevax)
        else: 
            nuevapalabra=nuevapalabra+chr(nuevax)
    return nuevapalabra