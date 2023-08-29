def jerigonzo(string):
    agrega = ""
    for letra in string:
        if letra in "AEIOUaeoiu":
            agrega += letra
            agrega += "p"
        agrega +=letra
    return agrega

string = input("ingrese su frase:")
print (jerigonzo(string))