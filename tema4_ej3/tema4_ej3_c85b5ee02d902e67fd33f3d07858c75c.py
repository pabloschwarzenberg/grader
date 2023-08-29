def traducir_a_jerigonzo(texto):
    resultado = ""
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    
    for letra in texto:
        if letra in vocales:
            resultado += letra + 'p' + letra.lower()
        else:
            resultado += letra
    
    return resultado

