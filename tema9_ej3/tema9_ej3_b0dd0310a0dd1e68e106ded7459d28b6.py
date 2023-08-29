def decodificar(mensaje):
    codigo = mensaje.split(",")
    lista = list(codigo)
    texto = ""
    while len(lista) > 0:
        if lista[0] == str("01100001"):
            texto = texto + "a"
            del lista[0]
            continue
        if lista[0] == str("01100010"):
            texto = texto + "b"
            del lista[0]
            continue
        if lista[0] == str("01100011"):
            texto = texto + "c"
            del lista[0]
            continue
        if lista[0] == str("01100100"):
            texto = texto + "d"
            del lista[0]
            continue
        if lista[0] == str("01100101"):
            texto = texto + "e"
            del lista[0]
            continue
        if lista[0] == str("01100110"):
            texto = texto + "f"
            del lista[0]
            continue
        if lista[0] == str("01100111"):
            texto = texto + "g"
            del lista[0]
            continue
        if lista[0] == str("01101000"):
            texto = texto + "h"
            del lista[0]
            continue
        if lista[0] == str("01101001"):
            texto = texto + "i"
            del lista[0]
            continue
        if lista[0] == str("01101010"):
            texto = texto + "j"
            del lista[0]
            continue
        if lista[0] == str("01101011"):
            texto = texto + "k"
            del lista[0]
            continue
        if lista[0] == str("01101100"):
            texto = texto + "l"
            del lista[0]
            continue
        if lista[0] == str("01101101"):
            texto = texto + "m"
            del lista[0]
            continue
        if lista[0] == str("01101110"):
            texto = texto + "n"
            del lista[0]
            continue
        if lista[0] == str("01101111"):
            texto = texto + "o"
            del lista[0]
            continue
        if lista[0] == str("01110000"):
            texto = texto + "p"
            del lista[0]
            continue
        if lista[0] == str("01110001"):
            texto = texto + "q"
            del lista[0]
            continue
        if lista[0] == str("01110010"):
            texto = texto + "r"
            del lista[0]
            continue
        if lista[0] == str("01110011"):
            texto = texto + "s"
            del lista[0]
            continue
        if lista[0] == str("01110100"):
            texto = texto + "t"
            del lista[0]
            continue
        if lista[0] == str("01110101"):
            texto = texto + "u"
            del lista[0]
            continue
        if lista[0] == str("01110110"):
            texto = texto + "v"
            del lista[0]
            continue
        if lista[0] == str("01110111"):
            texto = texto + "w"
            del lista[0]
            continue
        if lista[0] == str("01111000"):
            texto = texto + "x"
            del lista[0]
            continue
        if lista[0] == str("01111001"):
            texto = texto + "y"
            del lista[0]
            continue
        if lista[0] == str("01111010"):
            texto = texto + "z"
            del lista[0]
            continue
    return (texto)