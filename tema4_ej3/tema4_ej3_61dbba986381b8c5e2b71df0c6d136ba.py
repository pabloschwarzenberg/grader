def jerigonzo(A):
    Vacia_Palabra = ""
    for cont in A:
        Vacia_Palabra += cont
        if cont in "AEIOUaeiou":
            Vacia_Palabra += "p"
            Vacia_Palabra += cont

    return Vacia_Palabra

if __name__ == "__main__":
    a = "estamos programando..."
    print(jerigonzo(a))

         