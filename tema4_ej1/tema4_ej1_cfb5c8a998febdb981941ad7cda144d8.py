#Adivina la palabra
import random
palabras= ["felicidad","sonrisa","universo","galaxias","constelacion","nebulosa","amor"]
palabra= random.choice(palabras)
cantidad= random.choice(range(1,len(palabra)))
def ocultar_letras(palabra, cantidad):
    palabra_1= list(palabra)
    i = 0
    while i < cantidad:
        s= random.choice(range(0,len(palabra)))
        if palabra_1[s] != "_":
            palabra_1[s]= "_"
        else:
            continue
        i = i + 1
    palabra_2 = "".join(palabra_1)
    return palabra_2
def revisar_letra(palabra_secreta,palabra,letra):
    palabrasecreta1= list(palabra_secreta)
    palabra1= list(palabra)
    for i in palabra1:
        if i == "_":
            s = palabra1.index(i)
            if palabrasecreta1[s] == letra:
                palabra1[s] = letra
    palabra3 = "".join(palabra1)
    return palabra3