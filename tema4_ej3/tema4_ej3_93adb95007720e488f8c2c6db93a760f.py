def jerigonzo(string):
    traduccion = ""
    for letra in string:
            if letra in "aeiou":
                traduccion += letra
                traduccion += "p"
            traduccion += letra

    return traduccion


if __name__ == "__main__":
    string = input("Ingrese una palabra: ")
    print(jerigonzo(string))
