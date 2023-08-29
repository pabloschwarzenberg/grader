def decodificar(mensaje):
    number = mensaje.split(",")
    number = "".join(number)
    empty_list = []
    i = 0
    o = 0
    j = 8
    while j <= len(number):
        integer = int(number[o:j], 2)
        empty_list.append(integer)
        i += 1
        o += 8
        j += 8
    palabra = []
    for i in range(len(empty_list)):
        asci = chr(empty_list[i])
        palabra.append(asci)

    palabra = "".join(palabra)
    return palabra