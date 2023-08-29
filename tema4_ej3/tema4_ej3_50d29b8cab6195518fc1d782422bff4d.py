def traducir_a_jerigonzo(texto):
    resultado = ""
    for letra in texto:
        if letra.lower() in "aeiouáéíóú":
            resultado += letra + "p" + letra.lower()
        else:
            resultado += letra
    return resultado

if __name__ == "__main__":
    texto_original = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto_original)
    print("Texto traducido a jerigonzo: ", texto_traducido)


 