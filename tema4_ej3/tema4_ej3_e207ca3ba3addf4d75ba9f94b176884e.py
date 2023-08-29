def traducir_a_jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_jerigonzo = ""
    
    for letra in texto:
        if letra.lower() in vocales:
            texto_jerigonzo += letra + "p" + letra.lower()
        else:
            texto_jerigonzo += letra
    
    return texto_jerigonzo

# Ejemplo de uso
texto = "Hola, cómo estás?"
texto_traducido = traducir_a_jerigonzo(texto)
print(texto_traducido)
