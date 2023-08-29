def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouAEIOU"
    for caracter in texto:
        jerigonzo += caracter
        if caracter.lower() in vocales:
            jerigonzo += "p" + caracter.lower()
    return jerigonzo

if __name__ == "__main__":
    texto = input("Ingrese el texto a traducir: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:")
    print(texto_traducido)