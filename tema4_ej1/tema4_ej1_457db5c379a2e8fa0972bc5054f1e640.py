import random

def ocultar_letras(palabra,cantidad):
    contador=1
    while contador<=cantidad:
        a=True
        while a:
            l=random.randint(0,len(palabra)-1)
            if palabra[l]!='_':
                palabra=palabra[0:l]+'_'+palabra[l+1:len(palabra)]
                contador=contador+1
                a=False
            else:
               n=random.randint(0,len(palabra)-1)
               palabra=palabra.replace(palabra[n],'_')
               contador+=1
               a=True
    return palabra

def revisar_letra(palabra_secreta, palabra, letra):
    lista=[]
    for i in range(len(palabra_secreta)):
        if palabra_secreta[i]==letra:
            lista.append(i)
    print(lista)
    for i in lista:
        palabra=palabra[0:i]+ letra + palabra[i+1:len(palabra)]
    return palabra
    