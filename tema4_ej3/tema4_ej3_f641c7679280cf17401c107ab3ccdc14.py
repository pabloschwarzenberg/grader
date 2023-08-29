def jerigonzo(texto):
    renombrado = []
    for palabra in texto:
        for letra in palabra:
            if letra in "aeiouáéíóúAEIOUÁÉÍÓÚ":
                letra = letra + "p" + letra
            renombrado.append(letra)
    renombrado = "".join(renombrado)
    return renombrado

if __name__ == "__main__":
    a = input("Ingrese una palabras u oración: ")
    print(jerigonzo(a))