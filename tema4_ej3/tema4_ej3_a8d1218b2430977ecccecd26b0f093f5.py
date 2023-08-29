def traduccion(txt):
    jerigonzo = ""
    vocal = ""
    for letra in txt:
        if letra in "aeiou":
            vocal = letra
    jerigonzo = txt + "p" + vocal
    return jerigonzo

if __name__ == "__main__":
    palabra = input("Ingrese una palabra: ")
    print(traduccion(palabra))
    pass
         