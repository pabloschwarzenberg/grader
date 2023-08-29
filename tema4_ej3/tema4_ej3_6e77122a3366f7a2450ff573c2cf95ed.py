def jerigonzo(tj):
    a = ""
    for letra in tj:
        if letra in "AEIOUaeiou":
            a +=letra
            a += "p"
        a += letra
    return a
if __name__ == "__main__":
    palabra = input("ingresa una palabra:")
    print(traductor(palabra))