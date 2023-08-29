def jerigonzo(STR):
    x = []
    for Palabra in STR:
        for L in Palabra:
            if (L in "AEIOUaeiou"):
                L = L + "p"+ L
            x.append(L)
    x = "".join(x)
    
    return x
if __name__ == "__main__":
    pass
         