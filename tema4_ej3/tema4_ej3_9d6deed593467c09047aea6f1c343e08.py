def jerigonzo(string):
    nuevo_texto = ""
    for letra in string:
        if letra in "aeiouAEIOU":
            nuevo_texto += letra + "p" + letra.lower()
        else:
            nuevo_texto += letra
    return nuevo_texto
    return string

if __name__ == "__main__":
    texto_prueba = input("Ingresa un texto: ")
    traduccion = traducir_jerigonzo(texto_prueba)
    print(traduccion)
    pass
         