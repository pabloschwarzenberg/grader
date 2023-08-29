import random

lista_palabras=["lepidoptero",'dinosaurio','manzana','arbol','ovni']

def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    p=len(palabra)
    i=0
    while True:
        x=random.randint(0,p-1) #x=posicion aleatoria
        if palabra[x]!='_':
            palabra.pop(x)
            palabra.insert(x,"_")
            i=i+1
        if i==cantidad:
            break
    return "".join(palabra)

def revisar_letra(palabra_secreta,palabra,letra):
    palabra=list(palabra)
    for i in range(len(palabra)):
        if palabra_secreta[i]==letra:
            palabra.pop(i)
            palabra.insert(i,letra)
    return "".join(palabra)



