def jerigonzo(string):
    lista=[]
    for i in ["a", "e", "i","o","u"]:
        string = string.replace(i,i + "p" + i)
        lista.append(string)
    return lista[4]
if __name__ == "__main__":
    jerigonzo(input())
