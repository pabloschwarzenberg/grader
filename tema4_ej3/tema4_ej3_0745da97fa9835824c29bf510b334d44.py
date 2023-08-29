def convertir_a_jerigonzo(texto):
    vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    resultado = ""
    for letra in texto:
        if letra in vocales:
            resultado += letra + 'p' + letra.lower()
        else:
            resultado += letra
    return resultado

if __name__ == '__main__':
    texto = input("Ingresa un texto para convertir a jerigonzo: ")
    texto_jerigonzo = convertir_a_jerigonzo(texto)
    print("Texto original: ", texto)
    print("Texto en jerigonzo: ", texto_jerigonzo)
