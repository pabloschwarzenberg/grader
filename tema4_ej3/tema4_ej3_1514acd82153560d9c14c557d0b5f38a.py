def jerigonzo(string):
    jerigonzo = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            jerigonzo += letra
            jerigonzo += "p"
        jerigonzo += letra
    return jerigonzo
#print(jerigonzo(input("Ingresa una frase: \n>")))

#if __name__ == "__main__":
#print(jerigonzo(input("Ingresa una frase: \n>")))
 #   pass
         