import random

def ocultar_letras(palabra, cantidad):
    list = []
    for i in palabra:
        list.append(i)
    i = 0
    while i < cantidad:
        x = random.randint(0, len(palabra)-1)
        if list[x] != "_":
            list.insert(x, "_")
            i = i + 1
            del list[x+1]
    palabra_oculta = "".join(list)
    return palabra_oculta

def revisar_letra(palabra_secreta, palabra, letra):
    list = []
    for i in palabra:
        list.append(i)

    cont = 0
    for j in palabra:
        cont += 1
        if j == "_" and palabra_secreta[cont-1] == letra:
            list[cont-1] = palabra_secreta[cont-1]
    respuesta = "".join(list)
    return respuesta

if __name__ == "__main__":
    pass
         