def jerigonzo(string):
    traducida = ""
    for letra in string:
        traducida += letra
        if letra.lower() in "aeiou":
            traducida += "p" + letra
    return traducida

if __name__ == "__main__":
    palabra = input("Escribe una palabra: ")
    traducida = jerigonzo(palabra)
    print(traducida)
    pass      