def jerigonzo(string):
    string.lower()
    traduccion = ""
    for i in string:
        if i in "aeiouy":
            traduccion += i

            traduccion += "p"
        traduccion += i

    

    return traduccion


if __name__ == "__main__":
    string = input("ingrese texto: ")
    print(jerigonzo(string))

    pass