def jerigonzo(string):
    agrego = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            agrego = agrego + letra
            agrego = agrego + "p"
        agrego = agrego + letra
    return agrego
if __name__ == "__main__":
    palabra = str(input(" ingrese :"))
    print (jerigonzo(palabra))
    pass