def jerigonzo(string):
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    A = "A"
    E = "E"
    I = "I"
    O = "O"
    U = "U"

    nuevaPalabra = ""
    for letra in string:
        if(letra != a and letra != e and letra != i and letra != o and letra != u and letra != A and letra != E and letra != I and letra != O and letra != U):
            nuevaPalabra += letra
        else:
            nuevaPalabra += ((letra) + ("p") + (letra.lower()))
    return nuevaPalabra


         