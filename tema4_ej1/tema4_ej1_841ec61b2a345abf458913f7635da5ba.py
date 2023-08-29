import random
def ocultar_letras(palabra,cantidad):
    letras_ocultas = random.sample(range(len(palabra)), cantidad)
    palabra_oculta = list(palabra)

    for indice in letras_ocultas:
        palabra_oculta[indice] = "_"

    return "".join(palabra_oculta)

def revisar_letra(palabra_secreta,palabra_mostrada,letra):
    nueva_palabra_mostrada = list(palabra_mostrada)

    for i in range(len(palabra_secreta)):
        if palabra_secreta[i] == letra:
            nueva_palabra_mostrada[i] = letra

    return "".join(nueva_palabra_mostrada)


if __name__ == "__main__":
    pass
         