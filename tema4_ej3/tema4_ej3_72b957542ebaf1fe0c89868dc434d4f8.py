def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouAEIOU"
    
    for caracter in texto:
        jerigonzo += caracter
        if caracter in vocales:
            jerigonzo += "p" + caracter.lower()
    
    return jerigonzo

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
