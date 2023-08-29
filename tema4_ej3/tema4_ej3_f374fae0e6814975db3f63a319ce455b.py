def traducir_a_jerigonzo(texto):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    resultado = ''

    for letra in texto:
        resultado += letra
        if letra in vocales:
            resultado += 'p' + letra.lower()

    return resultado
if __name__ == "__main__":
    texto = input("Ingresa un texto: ")
    texto_traducido = traducir_a_jerigonzo(texto)
    print(texto_traducido)
