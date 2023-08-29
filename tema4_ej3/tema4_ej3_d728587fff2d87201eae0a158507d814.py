def jerigonzo(string):
    palabra_nueva=list(string)
    for letra in range(0,len(palabra_nueva)):
        if "a"==string[letra] or "e"==string[letra] or "i"==string[letra] or "o"==string[letra] or "u"==string[letra]:
            palabra_nueva[letra]+="p"+palabra_nueva[letra]
    return "".join(palabra_nueva)

if __name__ == "__main__":
    palabra=str(input("Ingrese una palabra: "))
    print(jerigonzo(palabra))
         