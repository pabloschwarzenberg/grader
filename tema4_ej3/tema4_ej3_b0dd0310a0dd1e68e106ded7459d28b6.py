def jerigonzo(string):
    l = list(string)
    texto = ""
    while len(l) > 0:
        if l[0] == str("A") or l[0] == str("a"):
            texto = texto + "".join(l[0]) + "pa"
            del l[0]
            continue
        if l[0] == str("E") or l[0] == str("e"):
            texto = texto + "".join(l[0]) + "pe"
            del l[0]
            continue
        if l[0] == str("I") or l[0] == str("i"):
            texto = texto + "".join(l[0]) + "pi"
            del l[0]
            continue
        if l[0] == str("O") or l[0] == str("o"):
            texto = texto + "".join(l[0]) + "po"
            del l[0]
            continue
        if l[0] == str("U") or l[0] == str("u"):
            texto = texto + "".join(l[0]) + "pu"
            del l[0]
            continue
        else:
            texto = texto + "".join(l[0])
            del l[0]
            continue
    return (texto)
