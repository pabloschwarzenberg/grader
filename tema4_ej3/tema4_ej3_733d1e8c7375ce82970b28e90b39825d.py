def jerigonzo(string):
    vocales=["a","e","i","o","u"]
    string=list(string)
    jerigonzo=[]
    for caracter in string:
        if caracter in vocales:
            jerigonzo.append(caracter+"p"+caracter)
        else:
            jerigonzo.append(caracter)
    string="".join(jerigonzo)
    return string

if __name__ == "__main__":
    string=input("Ingrese texto: ")
    print(jerigonzo(string))
