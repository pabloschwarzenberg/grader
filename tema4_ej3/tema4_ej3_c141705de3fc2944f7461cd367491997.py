def jerigonzo(palabra):
    vocales = ["a","e","i","o","u"]
    lis = []
    for car in palabra: #"hola"
        lis.append(car)
        if car in vocales:
            lis.append("p")
            lis.append(car)
    fraseJoin = ''.join(lis)
    return fraseJoin
print(jerigonzo("hola"))