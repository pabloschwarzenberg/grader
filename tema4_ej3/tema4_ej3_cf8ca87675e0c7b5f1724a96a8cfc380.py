def jerigonzo(texto):
    texto_traducido = ""
    for caracter in texto:
        if caracter.lower() in "aeiouáéíóú":
            texto_traducido += caracter + "p" + caracter.lower()
        else:
            texto_traducido += caracter
    return texto_traducido

if __name__ == "__main__":
    o = jerigonzo("estamos programando")
    print(o)
