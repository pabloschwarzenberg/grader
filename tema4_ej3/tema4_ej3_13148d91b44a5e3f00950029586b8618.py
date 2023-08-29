def traducir_a_jerigonzo(texto):
    jerigonzo = ""
    vocales = "aeiouAEIOU"
    for letra in texto:
        if letra in vocales:
            jerigonzo += letra + "p" + letra.lower()
        else:
            jerigonzo += letra
    return jerigonzo

# Ejemplo de uso
texto_original = "Hola, ¿cómo estás?"
texto_traducido = traducir_a_jerigonzo(texto_original)
print(texto_traducido)
