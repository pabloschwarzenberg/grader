import random

def ocultar_letras(palabra,cantidad):
    lista=list(palabra)
    contador=1
    while contador<=cantidad:
        ocultar=random.randint(0,len(palabra))
        lista[ocultar]='_'
        contador+=1
    palabra=''.join(lista)
    return palabra


def revisar_letra(palabra_secreta,palabra,letra):
    
    lista_palabra=list(palabra)
    lista_secreta=list(palabra_secreta)
    if letra in palabra_secreta:
        vacio=[]
        for i in range(len(lista_secreta)):    
            if lista_secreta[i]==letra:    
                vacio.append(i)
    #tengo la lista vacio donde estan las posciciones de la letra en la palabra
        for j in vacio:
            lista_palabra[j]=letra

    palabra=''.join(lista_palabra)
    palabra_secreta=''.join(lista_secreta)
    return palabra

if __name__ == "__main__":
    pass
         