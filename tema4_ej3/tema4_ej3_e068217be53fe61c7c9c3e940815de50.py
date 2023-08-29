def jerigonzo(string):
    p="p"
    vocal='a e i o u '.split()
    lista=list(string)

    for i in range (len(lista)):
        for x in range (len(vocal)):
            if lista[i]==vocal[x]:
                lista[i]=vocal[x]+p+vocal[x]
    string = (''.join(lista))
    return string