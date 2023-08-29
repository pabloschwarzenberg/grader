import random
def ocultar_letras(palabra,cantidad):
    x = list(palabra)
    for i in range(0,cantidad):
        Sub_cambiado = False
        while Sub_cambiado == False:
            y=random.randint(0,len(palabra)-1)
            if x[y] != '_':
                x[y] = '_'
                Sub_cambiado = True
    return ''.join(x)
def revisar_letra(palabra_secreta,palabra,letra):
    x=list(palabra)
    for i in range(0,len(palabra)):
        if palabra[i] == '_':
            if palabra_secreta[i]==letra:
                x[i]= letra
    return ''.join(x)