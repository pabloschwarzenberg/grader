def jerigonzo(string):
    #palabra
    w = ''
    
    for letra in string:
        if letra in "AEIOUaeiou":
            w += letra
            w += "p"
        w += letra
    if __name__ == "__main__":
        print(w)
    return w

if __name__ == "__main__":
    palabra = input("ingresa una palabra: ")
    jerigonzo(palabra)
    pass