def jerigonzo(frase):

    a = frase.replace("a", "apa")
    
    a = a.replace("e", "epe")

    a = a.replace("i","ipi")

    a = a.replace("o", "opo")

    a = a.replace("u", "upu")

    return a


if __name__ == "__main__":
    a = str(input("Ingrese el texto: "))
    mj = jerigonzo(a)
