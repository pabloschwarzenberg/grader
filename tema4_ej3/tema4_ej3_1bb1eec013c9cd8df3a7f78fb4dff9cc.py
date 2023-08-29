def jerigonzo(string):
    jerigonzo=""
    for letra in string:
        if letra in "AEIOUaeiou":
            jerigonzo += letra
            jerigonzo += "p"
        jerigonzo += letra
    return jerigonzo

if __name__ == "__main__":
    frase=(input("Ingresa una frase: "))
    cambio=jerigonzo(frase)
    print(cambio)
   

         