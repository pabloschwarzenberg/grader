def ocultar_letras(palabra,cantidad):
    import random
    palabra_lista=list(palabra)
    while cantidad>0:
        index=random.randint(0,len(palabra)-1)
        palabra_lista[index]='_'
        cantidad-=1
    return ''.join(palabra_lista)
        
def revisar_letra(palabra_secreta,palabra,letra):
    palabra_secreta_lista=list(palabra_secreta)
    palabra_lista=list(palabra)
    i=0
    while i<len(palabra):
        if palabra_secreta_lista[i]==letra and palabra_lista[i]=='_':
            palabra_lista[i]=letra
        i+=1
    return ''.join(palabra_lista)

                   