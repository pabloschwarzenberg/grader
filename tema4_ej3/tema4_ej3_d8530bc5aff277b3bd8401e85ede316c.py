def jerigonzo(palabra):
    vocales=["a","e","i","o","u"]
    lis=[]
    for c in palabra:
        lis.append(c)
        if c in vocales:
            lis.append("p")
            lis.append(c)
    fraseJoin= "".join(lis)
    return fraseJoin

if __name__ == "__main__":
    pass
