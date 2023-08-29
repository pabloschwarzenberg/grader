def jerigonzo(texto):
    vocales = "aeiouáéíóú"
    texto_traducido = ""
    
    for letra in texto:
        if letra.lower() in vocales:
            texto_traducido += letra + "p" + letra.lower()
        else:
            texto_traducido += letra
    
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)
