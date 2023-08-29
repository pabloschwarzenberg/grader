def traducir_a_jerigonzo(texto):
    vocales = "aeiouáéíóú"
    resultado = ""
    for letra in texto:
        resultado += letra
        if letra.lower() in vocales:
            resultado += "p" + letra.lower()
    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    resultado = traducir_a_jerigonzo(texto)
    print("El texto en jerigonzo es:", resultado)
