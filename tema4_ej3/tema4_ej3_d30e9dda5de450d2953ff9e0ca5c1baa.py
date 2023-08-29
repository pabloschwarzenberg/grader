def traducir_a_jerigonzo(texto):
    texto_jerigonzo = ""
    for letra in texto:
        if letra.lower() in "aeiou":
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra
    return texto_jerigonzo

if __name__ == "__main__":
    texto_entrada = input("Ingrese el texto a traducir: ")
    texto_traducido = traducir_a_jerigonzo(texto_entrada)
    print("Texto traducido a jerigonzo:", texto_traducido)