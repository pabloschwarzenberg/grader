import random
def ocultar_letras(palabra,cantidad):
    new = list(palabra)
    for i in range(0,cantidad):
        cambiado = False
        while cambiado == False:
            n=random.randint(0,len(palabra)-1)
            if new[n] != '_':
                new[n] = '_'
                cambiado = True
    return ''.join(new)
def revisar_letra(palabra_secreta,palabra,letra):
    new=list(palabra)
    for i in range(0,len(palabra)):
        if palabra[i] == '_':
            if palabra_secreta[i]==letra:
                new[i]= letra
    return ''.join(new)