import random
lista_secreta = ["coigue", "canelo", "ñirre", "eucalipto", "lenga", "maiten"]

i = random.randint(0,5)
palabra_secreta = lista_secreta[i]
palabra = list(palabra_secreta)
cantidad = random.randint(0,len(palabra))

def ocultar_letras(palabra_secreta,cantidad):
    global palabra
    for i in range(0,cantidad + 1):
        x = random.randint(0, len(palabra) - 1)
        palabra[x]="_"
    palabra = "".join(palabra)
    return palabra

ocultar_letras(palabra_secreta,cantidad)
def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta = str(list(palabra_secreta))
    palabra = str(list(palabra))
    if str(letra) in palabra_secreta:
        n = palabra_secreta.index(letra)
        palabra[n] = letra
    return palabra
         