def jerigonzo(string):
    traduccion = ""
    for i in string:
        traduccion += i
        if i in "AEIOUaeiou":
            traduccion += "p"
            traduccion += i
    return traduccion

if __name__ == "__main__":
    palabra = input("Ingresa una palabra = ")
    pass
         