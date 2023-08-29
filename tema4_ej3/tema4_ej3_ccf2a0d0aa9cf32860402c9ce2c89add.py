def traducir_a_jerigonzo(texto):
    vocales = ['a', 'e', 'i', 'o', 'u']
    resultado = ""
    for letra in texto:
        resultado += letra
        if letra.lower() in vocales:
            resultado += 'p' + letra.lower()
    return resultado

if __name__ == "__main__":
    texto = input("Ingrese un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print("Texto traducido a jerigonzo:", texto_traducido)