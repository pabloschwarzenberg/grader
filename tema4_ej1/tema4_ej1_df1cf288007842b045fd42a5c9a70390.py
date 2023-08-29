import random
def ocultar_letras(palabra,cantidad):
    largo = len(palabra)
    for i in range(0, cantidad):
        while True:
            n = random.randint(0, largo - 1)
            if palabra[n] != '_':
                palabra = palabra[0: n] + "_" + palabra[n + 1: largo]
                break 
    return palabra  

def revisar_letra(palabra_secreta,palabra,letra):
    largo = len(palabra_secreta)
    for k in range(largo):
        if palabra_secreta[k] == letra and palabra[k] == '_':
            palabra = palabra[0: k] + letra + palabra[k + 1: largo]
        
    return palabra
