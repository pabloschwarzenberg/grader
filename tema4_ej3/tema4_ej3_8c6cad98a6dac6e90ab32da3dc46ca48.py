def jerigonzo(string):
    lista=[]
    vocales=['a','e','i','o','u']
    for i in string:
        lista.append(i)
        for y in vocales:
            if i==y:
                lista.append("p")
                lista.append(i)
    string= ''.join(lista)
    return string