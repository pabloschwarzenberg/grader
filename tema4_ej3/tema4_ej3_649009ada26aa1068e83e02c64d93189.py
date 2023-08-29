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
    resultado_jerigonzo = jerigonzo(texto)
    print("Texto traducido al jerigonzo:", resultado_jerigonzo)

         