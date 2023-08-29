def jerigonzo(string):
    return string

if __name__ == "__main__":
    pass
def jerigonzo(palabra):
    vocales = ["a","e","i","o","u"]
    lis = []
    for car in palabra:
        lis.append(car)
        if car in vocales:
            lis.append("p")
            lis.append(car)
    fraseJoin = ''.join(lis)
    return fraseJoin
print(jerigonzo("hola"))