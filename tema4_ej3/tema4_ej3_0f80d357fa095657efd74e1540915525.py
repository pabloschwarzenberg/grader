def jerigonzo(String):
    Traduccion = ""
    for i in String:
        Traduccion += i
        if i in "AeIoUaEiOu":
            Traduccion += "p"
            Traduccion += i
    return Traduccion

if __name__ == "__main__":
    Palabra = input("Ingresa una palabra = ")
    pass