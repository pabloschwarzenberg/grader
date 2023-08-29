def traducir_jerigonzo(texto):
    vocales = "aeiouAEIOU"
    resultado = ""
    for char in texto:
        if char in vocales:
            resultado += char + "p" + char
        else:
            resultado += char
    return resultado
texto = "Hola mundo"
texto_jerigonzo = traducir_jerigonzo(texto)
print(texto_jerigonzo)

         