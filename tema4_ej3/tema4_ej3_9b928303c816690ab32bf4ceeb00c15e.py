def jerigonzo(frase):
    frase1 = frase.replace("a", "apa")
    frase2 = frase1.replace("e", "epe")
    frase3 = frase2.replace("i", "ipi")
    frase4 = frase3.replace("o", "opo")
    frase5 = frase4.replace("u", "upu")
    return frase5

if __name__ == "__main__":
    frase = str(input("Ingrese una frase: "))
    frase = frase.lower()
    print(jerigonzo(frase))
         