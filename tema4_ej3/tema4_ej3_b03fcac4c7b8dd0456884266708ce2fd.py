def jerigonzo(string):
    jerigonzo = ""
    # Iterar por cada caracter del texto
    for caracter in string:
        # Verificar si el caracter es una vocal
        if caracter.lower() in "aeiouáéíóú":
            # Agregar la vocal al jerigonzo
            jerigonzo += caracter + "p" + caracter.lower()
        else:
            # Mantener el caracter original en el jerigonzo
            jerigonzo += caracter

    return jerigonzo

if __name__ == "__main__":
    string = input("Ingrese un texto: ")
    texto_traducido = jerigonzo(string)
    print(texto_traducido)

         