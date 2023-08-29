def ocultar_letras(palabra, cantidad):
    import random
    ocultadas = 0
    remplazo = "_"
    lista = list(palabra)
    while True:
        indice = random.randint(0, len(lista) - 1)
        if lista[indice] != remplazo:
            lista[indice] = remplazo
            ocultadas += 1
        if ocultadas == cantidad:
            break
    return "".join(lista)


def revisar_letra(palabra_secreta, palabra, letra):
    lista = list(palabra)
    remplazo = "_"
    for indice in range(0, len(palabra)):
        if palabra[indice] == remplazo and palabra_secreta[indice] == letra:
            lista[indice] = letra
    return "".join(lista)

if __name__ == "__main__":
    pass
         