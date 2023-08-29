def jerigonzo(string):
    codigo = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            codigo += letra
            codigo += "p"
        codigo += letra
    return codigo

if __name__ == "__main__":
    string = input("ingrese palabra: ")
    print(jerigonzo(string))
         