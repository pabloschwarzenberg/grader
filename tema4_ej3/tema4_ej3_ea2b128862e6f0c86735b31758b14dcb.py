def jerigonzo(string):
    newFrase = string.replace("a","apa").replace("e","epe").replace("i","ipi").replace("o","opo").replace("u","upu")
    return newFrase

if __name__ == "__main__":
    frase = str(input("Ingrese una frase: "))
    print(jerigonzo(frase))
         
