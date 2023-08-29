def jerigonzo(s):
    s=s.replace("a", "apa")
    s=s.replace("e", "epe")
    s=s.replace("i", "ipi")
    s=s.replace("u", "upu")
    s=s.replace("o", "opo")
    return s


if __name__ == "__main__":
    s=input("Ingrese texto a traducir: ")
    print(jerigonzo(s))

