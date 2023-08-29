def traducir_a_jerigonzo(texto):
    texto_traducido = ""
    for caracter in texto:
        if caracter.lower() in "aeiouáéíóú":
            texto_traducido += caracter + "p" + caracter.lower()
        else:
            texto_traducido += caracter
    return texto_traducido

if "__name__" == "__main__":
    texto = input("Ingrese el texto a traducir: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido:", texto_traducido)