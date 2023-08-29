def jerigonzo(string):
    pala = ''
    for letra in string:
        if letra in "AEIOUaeiou":
            pala += letra
            pala += "p"
        pala += letra
    if __name__ == "__main__":
        print(pala)
    return pala

if __name__ == "__main__":
    palabra = input("ingresa una palabra: ")
    jerigonzo(palabra)
    pass

