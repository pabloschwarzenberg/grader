def jerigonzo(string):
    salida = ""
    for b in string:
        if (b == ("a" or "A")or
            b == ("e" or "E")or
            b == ("i" or "I")or
            b == ("o" or "O")):
            salida += b + "p" + b
        else:
            salida += b
    return salida

if __name__ == "__main__":
    texto = input("Ingrese su texto: ")
    resultado = jerigonzo(texto)
    print("su texto traduciso a jerigonzo es",resultado)
         