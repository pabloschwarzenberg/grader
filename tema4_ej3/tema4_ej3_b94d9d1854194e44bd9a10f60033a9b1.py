if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_jerigonzo = jerigonzo(texto)
    print("Texto original: ", texto)
    print("Texto en jerigonzo: ", texto_jerigonzo)
def jerigonzo(texto):
    resultado = ""
    for letra in texto:
        if letra.lower() in "aeiou":
            resultado += letra + "p" + letra.lower()
        else:
            resultado += letra
    return resultado
