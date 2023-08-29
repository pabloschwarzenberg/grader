def traducir_a_jerigonzo(texto):
    texto_traducido = ""
    vocales = "aeiouAEIOU"

    for palabra in texto.split():
        nueva_palabra = ""
        for letra in palabra:
            nueva_palabra += letra
            if letra in vocales:
                nueva_palabra += "p" + letra.lower()
        texto_traducido += nueva_palabra + " "

    return texto_traducido.strip()

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)