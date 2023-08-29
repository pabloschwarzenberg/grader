def traducir_a_jerigonzo(texto):
    resultado = ""
    vocales = "aeiouAEIOU"

    for caracter in texto:
        resultado += caracter
        if caracter in vocales:
            resultado += "p" + caracter.lower()

    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print(f"Texto traducido a Jerigonzo: {texto_traducido}")
         