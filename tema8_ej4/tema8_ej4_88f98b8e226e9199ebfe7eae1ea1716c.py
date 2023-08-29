def rot13(palabra):
    movimiento = 13
    mensaje = ""
    if palabra == palabra.upper():
        lista = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
    else:
        lista = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    for i in palabra:
        if i in lista:
            mensaje += lista[(lista.index(i)+movimiento%(len(lista)))]
        else:
            mensaje += i
    return mensaje
           