def jerigonzo(texto):
    resultado = ""
    
    for caracter in texto:
        if caracter.lower() in "aeiouáéíóú":
            resultado += caracter + "p" + caracter.lower()
        else:
            resultado += caracter
    
    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)