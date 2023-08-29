def jerigonzo(string):
    string.lower()
    palabra = ""
    for i in string:
        if i in "aeiou":
            palabra += i
            palabra += "p"
        palabra += i
    return palabra

if __name__ == "__main__":
    string = input('Ingrese una palabra o un texto: ')
    print(jerigonzo(string))
    pass