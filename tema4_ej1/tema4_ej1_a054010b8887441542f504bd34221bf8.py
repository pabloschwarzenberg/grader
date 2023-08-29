import random
#ocultar letras 
def ocultar_letras(palabra,cantidad):
    ine = list(palabra)
    for i in range(0,cantidad):
        alterar = False
        while alterar == False:
            b=random.randint(0,len(palabra)-1)
            if ine[b] != '_':
                ine[b] = '_'
                alterar = True
    return ''.join(ine)
#revisar palabra secreta     
def revisar_letra(palabra_secreta,palabra,letra):
    ine=list(palabra)
    for m in range(0,len(palabra)):
        if palabra[m] == '_':
            if palabra_secreta[m]==letra:
                ine[m]= letra
    return ''.join(ine)
    #retornar si se acerto en la palabra 
