def jerigonzo(palabra):
    jepalabra=[]
    for letra in palabra:
        if letra == "a":
            jepalabra.append("apa")
        elif letra == "e":
            jepalabra.append("epe")
        elif letra == "i":
            jepalabra.append("ipi")
        elif letra == "o":
            jepalabra.append("opo")
        elif letra == "u":
            jepalabra.append("upu")
        else:
            jepalabra.append(letra)
    jepalabra="".join(jepalabra)
    return jepalabra