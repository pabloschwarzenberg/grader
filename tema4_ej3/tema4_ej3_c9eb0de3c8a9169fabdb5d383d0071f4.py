def traducir_a_jerigonzo(texto):
    vocales = "aeiou"
    resultado = ""
    for letra in texto:
        resultado += letra
        if letra.lower() in vocales:
            resultado += "p" + letra.lower()
    return resultado

if __name__ == "__main__":
    texto = input("Ingrese el texto a traducir: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print(texto_traducido)