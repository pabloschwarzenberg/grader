def jerigonzo(string):
    lista=list(string)
    listanueva=[]
    vocales=["a","i","u","e","o"]
    for x in lista:
        if x in vocales:
            listanueva.append(x)
            listanueva.append("p")
            listanueva.append(x)
        else:
            listanueva.append(x)
    string="".join(listanueva)
    return string


if __name__ == "__main__":
    pass
         