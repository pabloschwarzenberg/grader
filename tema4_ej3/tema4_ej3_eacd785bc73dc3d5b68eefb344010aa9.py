def jerigonzo(tj):
    a = ""
    for letra in tj:
        if letra in "AEIOUaeiou":
            a +=letra
            a += "p"
        a += letra
    return a
if __name__ == "main":
    palabra = input("ingresa una palabra:")
    print(traductor(palabra))