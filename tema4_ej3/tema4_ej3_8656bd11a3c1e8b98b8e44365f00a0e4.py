def jerigonzo(string):
    nuevo = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            nuevo += letra
            nuevo += "p"
        nuevo += letra
    string = nuevo

    return string

if __name__ == "__main__":
    pass
         