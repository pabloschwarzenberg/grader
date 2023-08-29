def jerigonzo(texto):
    texto_traducido = ""
    vocales = "aeiouAEIOU"
    
    for caracter in texto:
        if caracter in vocales:
            texto_traducido += caracter + "p" + caracter.lower()
        else:
            texto_traducido += caracter
    
    return texto_traducido

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido:", texto_traducido)

         