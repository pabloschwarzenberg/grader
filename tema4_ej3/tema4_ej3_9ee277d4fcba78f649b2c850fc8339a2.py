def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouáéíóú"
    
    for letra in texto:
        jerigonzo += letra
        if letra.lower() in vocales:
            jerigonzo += "p" + letra.lower()
    
    return jerigonzo
if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a Jerigonzo:", texto_traducido)
