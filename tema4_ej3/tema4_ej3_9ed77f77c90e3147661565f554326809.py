def traducir_jerigonzo(texto):
    texto_jerigonzo = ""
    for letra in texto:
        if letra.lower() in "aeiouáéíóú":
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra
    return texto_jerigonzo
if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_jerigonzo(texto)
    print("Texto traducido:", texto_traducido)
