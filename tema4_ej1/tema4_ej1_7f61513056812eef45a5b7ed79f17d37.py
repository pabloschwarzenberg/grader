#Adivina la palabra
import random
palabras_secreta=["celular","teclado","pantalla"]
g=random.randint(0,2)
palabra_secreta=palabras_secreta[g]

def ocultar_letras(palabra,cantidad):
    import random
    global palabra_secreta
    palabra = list(palabra_secreta)
    i = 0
    while i < cantidad:
        palabra = list(palabra)
        slot = random.randint(0, len(palabra) - 1)
        if palabra[slot] == "_":
            continue
        palabra[slot] = "_"
        palabra = "".join(palabra)

        i += 1

    return palabra

def revisar_letra(palabra_secreta,palabra,letra):
    if palabra_secreta.find(letra) == -1:
        print("Esa letra no está")
    else:
        slot = 0
        while True:
            slot = palabra_secreta.find(letra, slot)
            if slot == -1:
                break
            palabra = list(palabra)
            palabra[slot] = letra
            palabra = "".join(palabra)
            slot += 1
    return palabra

if __name__ == "__main__":
    pass