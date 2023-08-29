def traducir_a_jerigonzo(texto):
    resultado = ""
    vocales = "aeiouAEIOU"

    for letra in texto:
        resultado += letra
        if letra in vocales:
            resultado += "p" + letra.lower()

    return resultado
if __name__ == "__main__":
    texto_entrada = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto_entrada)
    print("Texto traducido a jerigonzo:", texto_traducido)