def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    tmp=list(string)
    for w in range(len(tmp)):
        if (tmp[w] in vocales):
            tmp[w]=tmp[w]+"p"+tmp[w]
    string=""
    for x in tmp:
        string=string+x
    return string
