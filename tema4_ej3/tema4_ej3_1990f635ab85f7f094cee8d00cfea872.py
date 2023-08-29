def jerigonzo(string):
    buscador = ""
    for vocal in string:
        if vocal in "AEIOUaeiou":
            buscador += vocal
            buscador += "p"
        buscador += vocal
    return buscador
if __name__=="__main__":
    string = str(input("Introduzca palabra:"))
    if __name__=="__main__":
        print(jerigonzo(string))
         