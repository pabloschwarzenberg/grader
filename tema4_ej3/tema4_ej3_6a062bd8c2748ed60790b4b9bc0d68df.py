def traducir_a_jerigonzo(texto):
    resultado = ""
    vocales = "aeiouAEIOU"

    for letra in texto:
        resultado += letra
        if letra in vocales:
            resultado += "p" + letra

    return resultado
if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido: ", texto_traducido)

