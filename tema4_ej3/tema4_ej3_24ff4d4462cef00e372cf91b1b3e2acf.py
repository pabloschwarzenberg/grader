def es_vocal(string):
    return string.upper() in ["A", "E", "I", "O", "U"]

def jerigonzo(string):
    ne= ""
    for y in string:
        if not es_vocal(y):
            ne += y
        else:
            ne += y + "p" + y
    return ne


if __name__ =="__main__":
    palabra= str(input("ingrese una palabra"))
    print(jeringozo(palabra))