def traducir_a_jerigonzo(texto):
    resultado = ""
    vocales = "aeiouáéíóú"
    
    for letra in texto:
        if letra.lower() in vocales:
            resultado += letra + "p" + letra.lower()
        else:
            resultado += letra
    
    return resultado

if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
