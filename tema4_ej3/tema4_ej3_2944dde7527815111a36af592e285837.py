def jerigonzo(string):
    p=""
    for letra in string:
        if letra in "AEIOUaeiou":
            p += letra
            p += "p"
        p+= letra
    if __name__=="__main__":
        print(p)
    return p

if __name__=="__main__":
    palabra=input("ingrese palabra:")
    jerigonzo(palabra)
    pass