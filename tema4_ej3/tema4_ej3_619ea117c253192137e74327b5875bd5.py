def es_vocal(string):
    return string.upper() in ["A", "E", "I", "O", "U"]

def jerigonzo(string):
    n =""
    for l in string:
        if not es_vocal(l):
            n += l
        else:
            n += l + "p" + l
    return n


if __name__ == "__main__":
    palabra = str(input("ingrese una palabra"))
    print(jeringozo(palabra))        