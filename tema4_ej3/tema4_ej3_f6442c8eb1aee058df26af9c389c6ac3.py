def jerigonzo(texto):
    resultado = ""
    vocales = "aeiouáéíóú"
    
    for caracter in texto:
        resultado += caracter
        if caracter.lower() in vocales:
            resultado += "p" + caracter.lower()
    
    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido:", texto_traducido)
