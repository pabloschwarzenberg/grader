def jerigonzo(string):
    traduccion = ""
    for i in string:
        traduccion += i
        if i in "AEIOUaeiou":
            traduccion += "p"
            traduccion += i
    return traduccion

    palabra = input("Ingresa una palabra = ")
    pass