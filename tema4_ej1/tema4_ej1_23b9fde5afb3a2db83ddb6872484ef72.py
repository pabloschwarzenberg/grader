from random import randint
def ocultar_letras(palabra, cantidad):
    l = []
    lista_p = list(palabra)
    n = randint(1, len(lista_p)-1)
    if n not in l:
      l.append(n)
      cantidad -= 1
      palabra[n] = "_"
    return ("".join(palabra))

def revisar_letra(palabra_secreta, palabra, letra):
    j = list(palabra_secreta)
    palabra = list(palabra)
    if letra in j:
        z = palabra_secreta.find("-")
        palabra[z] = letra
    palabra = "".join(palabra)
    return palabra
         