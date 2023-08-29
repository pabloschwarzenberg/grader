def jerigonzo(pal):
    trad=""
    for letra in pal:
        if letra in "AEIOUaeiou":
            trad += letra
            trad += "p"
        trad += letra
    return trad

if __name__ == "__main__":
    pal = input("ingresa una palabra: ")
    print(jerigonzo(pal))
    pass
         